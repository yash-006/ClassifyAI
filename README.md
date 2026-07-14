# 🧠 ClassifyAI

> AI-Powered Image Classification using Transfer Learning and PyTorch

ClassifyAI is a deep learning-based image classification system developed as part of the **GUVI HCL AI/ML Capstone Project**. The project compares multiple state-of-the-art CNN architectures on different datasets and provides an interactive Streamlit application for real-time image classification.

---

## 🚀 Features

- Image classification using Transfer Learning
- Interactive Streamlit web application
- Support for multiple image datasets
- Automatic selection of the best-performing model
- Real-time prediction
- Top-5 prediction probabilities
- Confidence score
- Inference time measurement
- Comprehensive model evaluation

---

## 📂 Supported Datasets

| Dataset | Classes |
|----------|---------|
| Animals | 90 |
| Butterflies | 75 |
| ImageNet10 | 10 |

---

## 🏆 Best Performing Model

Based on the experimental comparison, **ConvNeXt Tiny** achieved the best overall performance across the evaluated datasets.

| Dataset | Selected Model |
|----------|----------------|
| Animals | ConvNeXt Tiny |
| Butterflies | ConvNeXt Tiny |
| ImageNet10 | ConvNeXt Tiny |

---

## 🏗️ Project Structure

```text
ClassifyAI/
│
├── app.py
├── requirements.txt
├── README.md
├── src/
│   ├── inference.py
│   └── model_factory.py
│
├── configs/
├── models/
├── checkpoints/
├── reports/
├── Notebook1.ipynb
├── Notebook2.ipynb
└── Notebook3.ipynb
```

---

## 🧠 Deep Learning Models Evaluated

- AlexNet
- VGG16
- VGG19
- ResNet18
- ResNet34
- SEResNet50
- ConvNeXt Tiny

---

## 📊 Evaluation Metrics

- Accuracy
- Precision
- Recall
- Macro F1 Score
- Expected Calibration Error (ECE)
- Model Parameters
- MACs (Computational Complexity)
- Inference Time

---

## 🔄 Project Workflow

```text
Dataset Preparation
        │
        ▼
Transfer Learning
        │
        ▼
Model Training
        │
        ▼
Model Evaluation
        │
        ▼
Model Comparison
        │
        ▼
Best Model Selection
        │
        ▼
Streamlit Deployment
```

---

## 🖥️ Streamlit Application

The Streamlit application provides:

- Dataset selection
- Image upload
- Automatic best-model selection
- Prediction result
- Confidence score
- Top-5 predictions
- Inference time

---

## 🛠️ Technologies Used

- Python
- PyTorch
- Torchvision
- TIMM
- Streamlit
- NumPy
- Pandas
- Matplotlib
- Scikit-learn
- Google Colab
- VS Code

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/ClassifyAI.git
cd ClassifyAI
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## 📸 Screenshots

Add screenshots of:

- Home Page
- Image Upload
- Prediction Results
- Top-5 Predictions

---

## 📈 Results

ConvNeXt Tiny achieved the best balance of:

- High Accuracy
- High Macro F1 Score
- Low Calibration Error
- Fast Inference

making it the recommended model for deployment.

---

## 🔮 Future Improvements

- Cloud deployment
- Batch image prediction
- Mobile-friendly interface
- Explainable AI (Grad-CAM)
- Model quantization for faster inference

---

## 👨‍💻 Author

**Yash**

B.Tech Computer Science Engineering

---

## 📜 License

This project is developed for educational and learning purposes as part of the GUVI HCL AI/ML Capstone Project.