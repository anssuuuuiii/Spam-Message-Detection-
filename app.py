import streamlit as st
import pickle
import re
import nltk
from nltk.corpus import stopwords

# Download stopwords (only runs first time)
nltk.download('stopwords')

# Load saved model & vectorizer
model = pickle.load(open('model.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

# Preprocessing function (same as training)
def preprocess(text):
    text = text.lower()
    text = re.sub('[^a-z]', ' ', text)
    words = text.split()
    words = [word for word in words if word not in stopwords.words('english')]
    return ' '.join(words)

# UI Design
st.set_page_config(page_title="Spam Detector", page_icon="📧")

st.title("📧 Email Spam Detection App")
st.write("Enter an email message below to check whether it is Spam or Not.")

# Input box
input_text = st.text_area("✉️ Enter Email Text Here")

# Button
if st.button("🔍 Predict"):
    if input_text.strip() == "":
        st.warning("⚠️ Please enter some text")
    else:
        # Preprocess
        cleaned = preprocess(input_text)

        # Vectorize
        vector = vectorizer.transform([cleaned])

        # Predict
        result = model.predict(vector)

        # Output
        if result[0] == 1:
            st.error("🚫 This is a Spam Email")
        else:
            st.success("✅ This is NOT a Spam Email")