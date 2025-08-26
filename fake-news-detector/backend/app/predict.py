# backend/app/predict.py

import joblib
import re
import string
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')
STOPWORDS = set(stopwords.words('english'))

# Cargar modelo y vectorizador
model = joblib.load("model/model.pkl")
vectorizer = joblib.load("model/vectorizer.pkl")

# Función para limpiar texto
def clean_text(text: str) -> str:
    text = text.lower()
    text = re.sub(r'\d+', '', text)
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = ' '.join([word for word in text.split() if word not in STOPWORDS])
    return text

# Función de predicción
def predict_fake_news(title: str, content: str) -> dict:
    combined = title + " " + content
    cleaned = clean_text(combined)
    vect_text = vectorizer.transform([cleaned])
    prediction = model.predict(vect_text)[0]
    proba = model.predict_proba(vect_text)[0]

    return {
        "prediction": "Fake" if prediction == 0 else "Real",
        "confidence": float(round(max(proba) * 100, 2))

    }
