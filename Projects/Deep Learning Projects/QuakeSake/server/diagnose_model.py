import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np
import os

print("="*60)
print("MODEL DIAGNOSTIC TOOL")
print("="*60)

MODEL_PATH = os.path.join(os.path.dirname(__file__), "models", "best_model.keras")

print(f"\n1. Checking if model file exists...")
print(f"   Path: {MODEL_PATH}")
print(f"   Exists: {os.path.exists(MODEL_PATH)}")

if not os.path.exists(MODEL_PATH):
    print("   ❌ Model file not found!")
    exit(1)

print(f"   File size: {os.path.getsize(MODEL_PATH) / (1024*1024):.2f} MB")

print(f"\n2. Attempting to load model...")
try:
    model = load_model(MODEL_PATH, compile=False)
    print("   ✅ Model loaded successfully (without compile)")
except Exception as e:
    print("   ❌ Failed to load model!")
    print(f"   Error: {e}")
    exit(1)

print(f"\n3. Model Architecture Info:")
print(f"   Model name: {model.name}")
print(f"   Total layers: {len(model.layers)}")
print(f"   Input shape: {model.input_shape}")
print(f"   Output shape: {model.output_shape}")

print(f"\n4. First 5 layers:")
for i, layer in enumerate(model.layers[:5]):
    print(f"   Layer {i}: {layer.name} - {layer.__class__.__name__}")
    if hasattr(layer, 'input_shape'):
        print(f"           Input: {layer.input_shape}")
    if hasattr(layer, 'output_shape'):
        print(f"           Output: {layer.output_shape}")

print(f"\n5. Searching for 'stem_conv' layer...")
stem_conv_found = False
for layer in model.layers:
    if 'stem_conv' in layer.name.lower():
        stem_conv_found = True
        print(f"   Found: {layer.name}")
        print(f"   Type: {layer.__class__.__name__}")
        if hasattr(layer, 'input_shape'):
            print(f"   Input shape: {layer.input_shape}")
        if hasattr(layer, 'output_shape'):
            print(f"   Output shape: {layer.output_shape}")

if not stem_conv_found:
    print("   stem_conv layer not found in model")

print(f"\n6. Testing model with RGB input:")
test_rgb = np.random.rand(1, 224, 224, 3).astype(np.float32)
print(f"   Test input shape: {test_rgb.shape}")

try:
    output = model.predict(test_rgb, verbose=0)
    print("   ✅ Prediction successful!")
    print(f"   Output shape: {output.shape}")
    print(f"   Output value: {output[0][0]:.4f}")
except Exception as e:
    print("   ❌ Prediction failed!")
    print(f"   Error: {e}")

print("\n" + "="*60)
print("DIAGNOSIS COMPLETE")
print("="*60)
