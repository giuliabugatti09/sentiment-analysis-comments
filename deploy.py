import streamlit as st
import joblib
import os

# 1. Page Configuration
st.set_page_config(
    page_title="AI Movie Sentiment Analyzer",
    page_icon="🎬",
    layout="centered"
)

# 2. Custom CSS Styling for a professional look
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        height: 3.5em;
        background-color: #1E88E5;
        color: white;
        font-weight: bold;
    }
    .stTextArea>div>div>textarea {
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Model Loading Logic
@st.cache_resource
def load_assets():
    """
    Loads the trained model and vectorizer from the models directory.
    Using cache_resource to ensure it only loads once into memory.
    """
    # Assuming the professional structure: models/filename.pkl
    model_path = os.path.join('models', 'sentiment_model.pkl')
    vectorizer_path = os.path.join('models', 'vectorizer.pkl')
    
    model = joblib.load(model_path)
    vectorizer = joblib.load(vectorizer_path)
    return model, vectorizer

# Attempt to load assets
try:
    model, vectorizer = load_assets()
except FileNotFoundError:
    st.error("Model Error: '.pkl' files not found in 'models/' directory. Please verify file paths.")
    st.stop()

# 4. User Interface
st.title("🎬 Movie Review Sentiment AI")
st.markdown("""
**Deep Learning & NLP Analysis:** Enter a movie review below, and our Naive Bayes engine will classify the emotional tone behind the text.
""")

# Main input area
user_input = st.text_area("Your Review:", placeholder="Describe what you thought about the film...", height=150)

# Action button and Processing
if st.button("Predict Sentiment"):
    if user_input.strip() != "":
        with st.spinner('Calculating probabilities...'):
            # Transform text using loaded vectorizer
            vectorized_text = vectorizer.transform([user_input])
            
            # Prediction and Confidence level
            prediction = model.predict(vectorized_text)[0]
            probability = model.predict_proba(vectorized_text).max()

            # Result Display
            st.divider()
            if prediction == 'pos':
                st.balloons()
                st.success(f"### ✨ Result: **POSITIVE**")
                st.metric(label="Model Confidence", value=f"{probability*100:.2f}%")
            else:
                st.error(f"### 😡 Result: **NEGATIVE**")
                st.metric(label="Model Confidence", value=f"{probability*100:.2f}%")
    else:
        st.warning("Please enter some text before analyzing.")

# 5. Informational Sidebar
st.sidebar.title("About the Project")
st.sidebar.markdown("""
This application uses a **Multinomial Naive Bayes** classifier. 

- **Dataset:** NLTK Movie Reviews (IMDb corpus).
- **Technique:** Bag-of-Words with stop-word filtering.
- **Language:** English.
""")

st.sidebar.markdown("---")
st.sidebar.write("Developed by [Giulia Bugatti](https://www.linkedin.com/in/giulia-bugatti-fonseca-226955267/)")