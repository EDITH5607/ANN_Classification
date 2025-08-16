# 🧠 ANN Classification: Customer Churn Prediction

![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-red?style=for-the-badge)
![Keras](https://img.shields.io/badge/Model-Keras-blue?style=for-the-badge)
![Python](https://img.shields.io/badge/Language-Python-yellow?style=for-the-badge)

A complete end-to-end **Artificial Neural Network (ANN)** pipeline for **Customer Churn Prediction**, deployed via **Streamlit** for real-time interactive classification.

🔗 **Live Demo**: [ANN Classification App](https://annclassification-bqmnohnfqgbkn4scgdw6hf.streamlit.app/)

---

## 📌 Project Motivation

Customer churn is one of the most critical challenges faced by businesses. Identifying which customers are likely to leave helps in:

- Reducing revenue loss 💸
- Improving customer satisfaction 🤝
- Building targeted retention strategies 🎯

This project builds and deploys an **ANN-based classifier** to predict churn probability given customer details.

---

## 📊 Dataset

- **Source**: `Churn_Modelling.csv`
- **Rows**: 10,000 customers
- **Features**: 14 (categorical + numerical)
- **Target**: `Exited` (1 = Churned, 0 = Retained)

### Features Used

- `CreditScore`
- `Geography`
- `Gender`
- `Age`
- `Tenure`
- `Balance`
- `NumOfProducts`
- `HasCrCard`
- `IsActiveMember`
- `EstimatedSalary`

---

## 🧠 ANN Model

The ANN was built using **TensorFlow/Keras**.

### Architecture

- **Input Layer**: Encoded & scaled customer features
- **Hidden Layer 1**: Dense (units=6), activation = `relu`
- **Hidden Layer 2**: Dense (units=6), activation = `relu`
- **Output Layer**: Dense (units=1), activation = `sigmoid`

### Training Details

- **Loss**: Binary Crossentropy
- **Optimizer**: Adam
- **Metrics**: Accuracy
- **Epochs**: 100
- **Batch Size**: 32

---

## 📈 Model Performance

- **Training Accuracy**: \~86%
- **Test Accuracy**: \~85%
- **Confusion Matrix**: Balanced results between churned & non-churned customers

_(Insert confusion matrix/ROC curve plots here if available — taken from `experiments.ipynb`.)_

---

## 🎛️ Preprocessing

- **Categorical Encoding**

  - `Geography` → OneHotEncoded (`geo_onehot_encoder.pkl`)
  - `Gender` → LabelEncoded (`label_encoder_gender.pkl`)

- **Feature Scaling**

  - StandardScaler for numerical features (`standard_scaler.pkl`)

Pickle files ensure consistent preprocessing in deployment.

---

## 🚀 Deployment

- **Framework**: Streamlit
- **Files**:

  - `app.py` → Frontend interface
  - `model.h5` → Trained ANN model
  - `*.pkl` → Preprocessing artefacts

- **Platform**: Streamlit Cloud

### Hosted App

🔗 [Click Here to Try](https://annclassification-bqmnohnfqgbkn4scgdw6hf.streamlit.app/)

---

## 🛠️ Installation & Usage

### 1️⃣ Clone the Repo

```bash
git clone https://github.com/EDITH5607/ANN_Classification.git
cd ANN_Classification
```

### 2️⃣ Install Requirements

```bash
pip install -r requirements.txt
```

### 3️⃣ Run Locally

```bash
streamlit run app.py
```

App will run at **[http://localhost:8501/](http://localhost:8501/)**

---

## 📂 Repository Structure

```text
ANN_Classification/
│── app.py                      # Streamlit App
│── Churn_Modelling.csv         # Dataset
│── model.h5                    # Trained ANN model
│── geo_onehot_encoder.pkl      # One-hot encoder for Geography
│── label_encoder_gender.pkl    # Gender encoder
│── standard_scaler.pkl         # Feature scaler
│── requirements.txt            # Dependencies
│── experiments.ipynb           # Training & experimentation
│── prediction.ipynb            # Batch predictions
└── README.md                   # Project documentation
```

---

## 📬 Contact

- Author: **[EDITH5607](https://github.com/EDITH5607)**
- Live App: [Streamlit Demo](https://annclassification-bqmnohnfqgbkn4scgdw6hf.streamlit.app/)
- Issues: Use [GitHub Issues](https://github.com/EDITH5607/ANN_Classification/issues)

---

⭐ If you find this repo helpful, don’t forget to **star it**! ⭐

---
