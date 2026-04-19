import streamlit as st
import pickle
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Download NLTK data
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Load model files
tfidf = pickle.load(open('models/tfidf_vectorizer.pkl', 'rb'))
model = pickle.load(open('models/spam_classifier_model.pkl', 'rb'))

lemmatizer = WordNetLemmatizer()

def transform_text(text):
    text = text.lower()
    words = nltk.word_tokenize(text)
    words = [word for word in words if word.isalpha()]
    cleaned_words = [lemmatizer.lemmatize(w) for w in words if w not in stopwords.words('english')]
    return " ".join(cleaned_words)

# UI
st.title("📧 Spam Classifier")

input_sms = st.text_area("Enter Message")

if st.button("Predict"):
    if input_sms == "":
        st.warning("Enter message first")
    else:
        transformed = transform_text(input_sms)
        vector_input = tfidf.transform([transformed]).toarray()
        result = model.predict(vector_input)[0]

        if result == 1:
            st.error("🚨 Spam")
        else:
            st.success("✅ Not Spam")