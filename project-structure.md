sentiment-analysis-comments/

├── models/                   # Serialized model artifacts (Pickle files)
│   ├── sentiment_model.pkl
│   └── vectorizer.pkl
├── notebooks/                # Jupyter/Colab experiments and EDA
│   └── sentiment_analysis.ipynb
├── src/                      # Source code for the ML pipeline
│   ├── preprocess.py         # Text cleaning and tokenization logic
│   ├── train_model.py              # Script to re-train the model
│   └── visualize.py              # Helper functions (plotting, metrics)
├── app.py                    # Streamlit web application (renamed from deploy.py)
├── .gitignore                # Files to ignore (env, __pycache__, etc.)
├── LICENSE                   # Project license
├── README.md                 # Project documentation and instructions
└── requirements.txt          # Production dependencies
