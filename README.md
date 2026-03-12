# 🎭 NLP Sentiment Analysis: IMDb Review Classification

> **Natural Language Processing (NLP)** engine designed to classify movie reviews using a Multinomial Naive Bayes architecture. This project achieves an **80% accuracy rate** by implementing a robust text-processing pipeline.

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![NLTK](https://img.shields.io/badge/NLTK-3.6+-4EAA25?logo=python&logoColor=white)](https://www.nltk.org/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Latest-F7931E?logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)

---

## 🎯 Project Scope
The goal was to build a binary classifier capable of distinguishing between positive and negative sentiment in raw text. This is a foundational AI task with direct applications in customer feedback analysis and social media monitoring.



## 🏗️ Technical Pipeline: From Raw Text to Features
Text data requires rigorous cleaning before it can be processed by mathematical models. My pipeline includes:
* **Tokenization & Cleaning:** Removing punctuation, HTML tags, and noise.
* **Stopword Removal:** Filtering out high-frequency words that lack predictive signal.
* **Stemming:** Reducing words to their root form (e.g., "running" → "run") to decrease feature dimensionality.
* **Vectorization:** Transforming text into a numerical matrix (Bag-of-Words).

---

## 📊 Model Performance & Metrics
The **Multinomial Naive Bayes** algorithm was chosen for its high efficiency and performance with high-dimensional sparse data (text).

| Metric | Negative | Positive | Global Average |
| :--- | :---: | :---: | :---: |
| **Accuracy** | - | - | **80%** |
| **Precision** | 77% | 83% | 80% |
| **Recall** | 85% | 75% | 80% |
| **F1-Score** | 0.81 | 0.79 | 0.80 |



---

## 🧪 Theoretical Foundation
The model is based on the **Bayes' Theorem**, calculating the posterior probability of a class based on word frequency:

$$P(class|doc) \propto P(class) \times \prod P(word|class)$$

By applying **Laplace Smoothing**, the model ensures that new words found in testing don't result in zero probabilities, maintaining system robustness.

---

## 🚀 Usage & Deployment
### Fast Execution
```bash
# Install dependencies
pip install -r requirements.txt

# Download NLTK resources and run
python -c "import nltk; nltk.download('movie_reviews')"
python src/main.py
