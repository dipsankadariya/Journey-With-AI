from flask import Flask, jsonify, request, send_from_directory
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications import efficientnet
import numpy as np
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# first, lets load the model
MODEL_PATH = "./models/best_model.keras"
model = load_model(MODEL_PATH)
print("Model loaded successfully")

# then lets create temporary directory named 'uploads' where we will save uploaded files
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

 #Ttime to create the prediction route
@app.route("/predict", methods=["POST"])
def predict():
    try:
        # lets handle the file upload first 
        file = request.files.get('file')
        if not file or file.filename == '':
            return jsonify({"error": "No file uploaded"}), 400

        # save the file temporarily
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(file_path)

        # load image in RGB mode
        img = image.load_img(file_path, target_size=(224, 224), color_mode='rgb')
        img_array = image.img_to_array(img)
        print(f"Image array shape: {img_array.shape}")

        # expand dims and preprocess for EfficientNet
        img_array = np.expand_dims(img_array, axis=0)
        img_array = efficientnet.preprocess_input(img_array)

        # make prediction
        prediction = model.predict(img_array, verbose=0)[0][0]
        result = "Cracks Detected" if prediction > 0.5 else "No Cracks Detected"
        confidence = float(prediction if prediction > 0.5 else (1 - prediction))

        # and clean up uploaded file 
        os.remove(file_path)

        print(f"Returning: {result}, Confidence: {confidence * 100:.2f}%")

        # return the json
        return jsonify({
            "prediction": result,
            "confidence": f"{confidence * 100:.2f}%",
            "crack_probability": f"{prediction * 100:.2f}%",
            "safe_probability": f"{(1 - prediction) * 100:.2f}%"
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# serve the HTML homepage
@app.route("/")
def home():
    return send_from_directory('../frontend', 'index.html')

# serve static files (CSS, JS, images, etc.)
@app.route("/<path:filename>")
def serve_static(filename):
    return send_from_directory('../frontend', filename)

if __name__ == "__main__":
    app.run(debug=True)
