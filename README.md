# ♻️ Smart Waste Classification System

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![YOLOv8](https://img.shields.io/badge/Model-YOLOv8-green)
![Streamlit](https://img.shields.io/badge/Framework-Streamlit-red)

An end-to-end Computer Vision application capable of detecting and classifying waste materials into 6 categories to facilitate smart recycling processes. Powered by **YOLOv8** and deployed using **Streamlit**.

## 🚀 Live Demo
Try the app directly in your browser:
### [👉 Click Here to Open App](https://waste-detection-yolov8.streamlit.app/)
*(Please allow a few seconds for the app to wake up)*

---

## 🧠 Project Overview
Sorting waste at the source is a critical challenge in waste management. This project leverages Deep Learning to automatically identify waste types from images.

**Classes Detected:**
1.  🌱 **Biodegradable** (Organic waste)
2.  📦 **Cardboard**
3.  🥃 **Glass**
4.  ⚙️ **Metal**
5.  📄 **Paper**
6.  🥤 **Plastic**

## 🛠️ Tech Stack
* **Model:** YOLOv8 (You Only Look Once) - Fine-tuned on a custom dataset.
* **Web Framework:** Streamlit
* **Image Processing:** OpenCV & PIL
* **Language:** Python

## 📸 Screenshots
| Original Image | Detection Result |
|:---:|:---:|
|<img width="1054" height="637" alt="image" src="https://github.com/user-attachments/assets/8c3e0d35-7e8b-4c31-9ebe-8d2c8606b3ad" />|<img width="1054" height="637" alt="image" src="https://github.com/user-attachments/assets/8f88ba5f-d277-4172-9bf1-e7f10eae6543" />|

## 💻 How to Run Locally
If you want to run this project on your local machine:

1.  **Clone the repository**
    ```bash
    git clone [https://github.com/USERNAME_TUAN/garbage-detection-yolov8.git](https://github.com/USERNAME_TUAN/garbage-detection-yolov8.git)
    cd garbage-detection-yolov8
    ```

2.  **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the app**
    ```bash
    streamlit run app.py
    ```

## 📂 Dataset
The model was trained on the **Garbage Detection** dataset sourced from Kaggle. It contains labeled images of 6 waste categories, formatted for YOLO object detection.

* **Dataset Source:** [Kaggle - Garbage Detection](https://www.kaggle.com/datasets/viswaprakash1990/garbage-detection)
* **Credits:** Viswaprakash
* **License:** Open Source (Check Kaggle page for details)

---

## Dashboard Preview

<img width="1913" height="952" alt="{4A161018-8CD9-47AF-B196-75160BE60CAC}" src="https://github.com/user-attachments/assets/2c01fb7c-e564-49b5-b695-f438b35daeae" />

