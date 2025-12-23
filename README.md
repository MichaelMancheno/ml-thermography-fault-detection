# Machine Learning for Thermography Fault Detection

## 📌 Project Overview
This project applies Machine Learning techniques to the diagnosis of electrical equipment failures using thermographic images and electrical magnitudes. The objective is to evaluate and compare different ML models to determine the most effective approach for industrial fault detection.

This work is based on my undergraduate thesis in Industrial Maintenance Engineering.

---

## 🏭 Industrial Context
Thermographic inspection is widely used in preventive and predictive maintenance to detect abnormal temperature patterns in electrical components. However, interpreting thermograms can be subjective and highly dependent on expert knowledge.

This project aims to reduce subjectivity by integrating Machine Learning models capable of learning fault patterns from thermographic data combined with electrical measurements.

---

## 📊 Dataset
- Thermographic matrices extracted from electrical equipment inspections
- Electrical magnitudes associated with each thermogram
- High-dimensional data (up to ~76,800 features per sample)
- Dataset size limited due to real industrial constraints

> Due to confidentiality reasons, the full dataset is not publicly available. Sample or synthetic data may be provided for demonstration purposes.

---

## ⚙️ Models Implemented
The following models were implemented and evaluated:

- Random Forest
- Support Vector Machine (SVM)
- Convolutional Neural Network (CNN)
- XGBoost

---

## 📈 Evaluation Metrics
Models were evaluated using:
- Accuracy
- Log Loss

Log Loss was used as the primary metric to evaluate probabilistic performance and penalize overconfident incorrect predictions.

---

## 🧠 Model Selection Rationale
- Random Forest showed increased Log Loss when electrical magnitudes were added, indicating poor handling of additional information.
- SVM showed no improvement when additional variables were included.
- CNN achieved low Log Loss but showed signs of overfitting due to model complexity and limited data.
- XGBoost demonstrated a significant reduction in Log Loss when electrical magnitudes were included, indicating better generalization and robustness.

**Final selected model: XGBoost**

---

## 🧪 Project Structure
