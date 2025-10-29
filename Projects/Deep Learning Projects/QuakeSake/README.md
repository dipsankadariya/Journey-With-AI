# 🏠 SafeQuake v1.0 Overview

The idea for this project came when I was reading an article about earthquakes in Nepal — a country that’s highly prone to seismic activity. The **Gorkha earthquake of 2015** took many lives and destroyed numerous buildings.  

Even today, many houses still have structural damage, and people continue to live in them — which is extremely dangerous. Cracks and weak structural surfaces could cause life-threatening issues if another earthquake strikes in the future.

Hiring an engineer to assess structural damage can be expensive, and doing it yourself is often difficult. Therefore, our goal with this project is to leverage the power of **AI** so that anyone with a phone or computer can independently analyze damage in their home.  

This is just the **basic version** of the application we have in mind. We’re just starting out on this project, and over time we’ll continue to add more features to enhance it.

---

## 💻 Demo
A demo web application **is available for now**.  
Users can upload images of house walls and receive predictions on the presence of cracks.  

[![Watch Demo](https://img.shields.io/badge/Watch%20Demo-YouTube-red?logo=youtube)](https://youtu.be/_kttGX100O4?si=_G7M0GtHhLpiU_yZ)  
*Click the icon to watch a demo of the basic application completed so far.*

---

## 🏗️ Methodology & Architecture
We trained a deep learning model to detect surface cracks in concrete structures. The model we used is **EfficientNetB0 with transfer learning**, providing a strong balance of accuracy and efficiency.  

Model training has been completed, and we are currently integrating it into a web interface.  

We hope this will help people quickly and safely assess their house walls without the need for costly professional inspections.

---

## 📂 Dataset
**Concrete Crack Images for Classification**  
- 40,000 labeled images of concrete/wall surfaces  
- Two categories: `Crack` and `No Crack`  
- Images are RGB and resized to 224×224 pixels  

---

## 📊 Model Performance
The model **achieved high accuracy** in detecting structural cracks.

| Model | Dataset | Accuracy | Precision | Recall | F1-Score |
|--------|----------|-----------|------------|---------|-----------|
| EfficientNetB0 | Validation Set | 99.91% | 0.9987 | 0.9995 | 0.9991 |

**Confusion Matrix**

|                | Predicted No Crack | Predicted Crack |
|----------------|------------------|----------------|
| True No Crack  | 4075             | 5              |
| True Crack     | 2                | 3918           |

**Prediction Confidence**  
- **No Crack:** 0.0023  
- **Crack:** 0.9987  

---

## ⚙️ Current Status
- ✅ Initial model training completed  
- ✅ Initial frontend development completed  
- ✅ Initial backend integration completed  
- ✅ Currently, the application can **distinguish between cracked and non-cracked surfaces**  

---

## 🎯 Ongoing Improvements
Currently, the application can detect basic cracks, but in the future we aim to implement more advanced features. Our goals include:  

- Add support for scanning an entire building using multiple images  
- Detect cracks with severity levels (minor, moderate, severe)  
- Provide visual crack highlighting and localization on images  
- Generate PDF reports for building inspections  
- Develop a mobile-friendly version for on-site analysis  
- Integrate building layouts and floor plans for more comprehensive assessments  

These upgrades will make the application more powerful and easier for users to safely assess their homes.

---

## 💬 Feedback and Support
For feedback, issues, or support, please open an issue in this repository.

---

## 📜 License
This project is licensed under the **MIT License**.
