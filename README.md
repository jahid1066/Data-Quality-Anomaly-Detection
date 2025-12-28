# Data Quality Assessment & Anomaly Detection

## Project Overview
This project focuses on **data quality analysis** and **anomaly detection** using statistical and machine learning methods on a real-world financial transactions dataset. The goal is to identify data issues, detect unusual patterns, and compare traditional statistical techniques with modern ML-based approaches.

The project is designed to reflect **industry-grade data science workflows** commonly used in banking, insurance, and risk analytics.

---

## Dataset Description

- **Dataset:** Credit Card Transactions Dataset
- **Source:** ULB Machine Learning Group (Kaggle)
- **Link:** https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud
- **Records:** 284,807 transactions
- **Features:** 31 (Time, Amount, anonymized PCA components V1–V28)
- **Target Variable:** `Class` (0 = Normal, 1 = Fraud)

> Note: The dataset is highly imbalanced, making it ideal for anomaly detection use cases.

---


## 1. Data Quality Assessment

### Key Checks Performed
- Missing value analysis
- Duplicate record detection
- Descriptive statistics validation
- Structural integrity checks

### Summary Results
| Metric | Value |
|------|------|
| Rows | 284,807 |
| Columns | 31 |
| Missing Values | 0 |
| Duplicate Rows | 1,081 |

✔ No missing values  
 Presence of duplicate transactions (important for financial systems)

### Statistical Sanity Checks
Descriptive statistics confirm:
- PCA-transformed variables are centered around zero
- Presence of extreme values (expected in fraud-related data)
- Wide range in transaction amounts and time variable

---

## 2. Statistical Anomaly Detection

### Method Used
- **Z-Score Based Detection**
- Threshold: |Z| > 3
- Fully unsupervised

### Results
| Label | Count |
|------|------|
| Normal | 246,991 |
| Anomalous | 37,816 |

Interpretation:
- Z-score is sensitive to extreme values
- Over-detects anomalies in high-dimensional data
- Useful as a baseline method but not optimal alone

---

## 3. Machine Learning Anomaly Detection

### Model Used
- **Isolation Forest**
- Contamination rate: 1%
- Unsupervised learning

### Output
- Anomaly labels (`-1` = anomaly, `1` = normal)
- Continuous anomaly scores

### Anomaly Score Distribution
The distribution shows:
- Clear skewness
- Long tail representing anomalous transactions
- Effective separation between normal and suspicious behavior

Output saved as:
- `results/anomaly_scores.csv`
- `results/anomaly_plots.png`

---

## Key Insights & Comparison

| Method | Strengths | Limitations |
|------|----------|------------|
| Z-Score | Simple, interpretable | Poor in high dimensions |
| Isolation Forest | Scalable, robust | Requires contamination tuning |

 ML-based methods significantly outperform statistical baselines  
 Isolation Forest is better suited for real-world fraud detection  

---

## Business Relevance

This project simulates **real production use cases**, including:
- Data quality validation pipelines
- Fraud and risk monitoring
- Anomaly detection without labeled data
- Regulatory reporting and audit support

Applicable industries:
- Banking & Finance
- Insurance
- Healthcare billing
- Cybersecurity

---

## Technologies Used

- Python
- Pandas, NumPy
- Scikit-learn
- SciPy
- Matplotlib, Seaborn
- Jupyter Notebook

---

## How to Run the Project

# Clone repository
git clone https://github.com/jahid1066/Data-Quality-Anomaly-Detection.git

cd Data-Quality-Anomaly-Detection

# Install dependencies
pip install -r requirements.txt

# Launch notebooks
jupyter notebook

---

## Future Improvements

- Add autoencoder-based anomaly detection

- Implement real-time streaming detection

- Feature drift and data drift monitoring

- SHAP-based anomaly explanations

---

## Author
Md Jahidul Islam

---

## License
This project is for academic, educational, and portfolio purposes.

---

