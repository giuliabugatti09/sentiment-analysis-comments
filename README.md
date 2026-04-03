# 🎭 NLP Sentiment Analysis: IMDb Review Classification

> **Natural Language Processing (NLP)** engine designed to classify movie reviews using a Multinomial Naive Bayes architecture. This project implements a full pipeline from raw text processing to a live web deployment.

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![NLTK](https://img.shields.io/badge/NLTK-3.6+-4EAA25?logo=python&logoColor=white)](https://www.nltk.org/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Latest-F7931E?logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Cloud-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)

---

## 🎯 Project Overview
This project addresses the challenge of binary sentiment classification. By training on the IMDb corpus, the model learns to identify linguistic patterns that distinguish a positive review from a negative one. 

**Key Applications:**
* 🗣️ **Brand Monitoring:** Real-time social media sentiment tracking.
* 📈 **Market Research:** Automated analysis of customer feedback.
* 🎬 **Entertainment:** Scaling movie and content rating systems.

---

## 🏗️ Technical Pipeline
The transition from unstructured text to machine-readable features follows a rigorous NLP workflow:

1.  **Exploratory Data Analysis (EDA):** Identifying class balance and word frequency distributions.
2.  **Text Preprocessing:** * **Tokenization:** Breaking sentences into individual terms.
    * **Stopword Removal:** Eliminating noise words (e.g., "the", "a").
    * **Normalization:** Lowercasing and removing special characters.
3.  **Vectorization:** Converting text into a sparse matrix using `CountVectorizer` (Bag-of-Words).
4.  **Modeling:** Training a **Multinomial Naive Bayes** classifier with Laplace Smoothing ($alpha=1.0$).
5.  **Serialization:** Exporting model artifacts (`.pkl`) for inference using `joblib`.

---

## 📊 Performance Analysis

| Metric | Negative | Positive | Global Average |
| :--- | :---: | :---: | :---: |
| **Accuracy** | - | - | **80.0%** |
| **Precision** | 77% | 83% | 80.0% |
| **Recall** | 85% | 75% | 80.0% |
| **F1-Score** | 0.81 | 0.79 | 0.80.0 |

> *Insight: The model shows a slight bias towards identifying negative reviews (higher Recall), which is often preferable for identifying critical user pain points.*

---

## 🚀 Deployment & Usage

### 💻 Local Execution
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/giuliabugatti09/sentiment-analysis-comments.git](https://github.com/giuliabugatti09/sentiment-analysis-comments.git)
   cd sentiment-analysis-comments
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit App:**
   ```bash
   streamlit run app.py
   ```

---

## 🧪 Mathematical Foundation
The engine utilizes the **Multinomial Naive Bayes** algorithm, which assumes independence between features (words):

$$P(c|x) = \frac{P(x|c)P(c)}{P(x)}$$

Where:
* $P(c|x)$ is the posterior probability of class $c$ (positive/negative) given predictor $x$ (text).
* $P(x|c)$ is the likelihood of the word appearing in that class.

---

## 📂 Project Structure
```text
├── assets/               # Images and branding for README
├── models/               # Serialized .pkl files (Model & Vectorizer)
├── notebooks/            # Jupyter experiments & EDA
├── src/                  # Core logic & utility scripts
├── app.py                # Streamlit Web Interface
└── requirements.txt      # Project dependencies
```

---

## ✉️ Contact
**Giulia Bugatti** - [LinkedIn](https://www.linkedin.com/in/giulia-bugatti-fonseca-226955267/)
```