# backend/app/train_model.py
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import joblib
import nltk
import re
import string

nltk.download('stopwords')
from nltk.corpus import stopwords

STOPWORDS = set(stopwords.words('english'))

# ----------- FUNCIONES DE LIMPIEZA DE TEXTO ----------- #
def clean_text(text):
    text = text.lower()
    text = re.sub(r'\d+', '', text)
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = ' '.join([word for word in text.split() if word not in STOPWORDS])
    return text

# ----------- CARGA Y PREPROCESAMIENTO ----------- #
def load_and_preprocess():
    true_df = pd.read_csv("data/True.csv")
    fake_df = pd.read_csv("data/Fake.csv")

    true_df['label'] = 1
    fake_df['label'] = 0

    df = pd.concat([true_df, fake_df], ignore_index=True)
    df['text'] = df['title'] + " " + df['text']
    df['text'] = df['text'].apply(clean_text)

    return df[['text', 'label']]

# ----------- ENTRENAMIENTO DEL MODELO ----------- #
def train_model():
    df = load_and_preprocess()

    X = df['text']
    y = df['label']

    vectorizer = TfidfVectorizer(max_features=5000)
    X_vect = vectorizer.fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(X_vect, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier(n_estimators=100)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    print(classification_report(y_test, y_pred))

    # Guardar modelo y vectorizador
    joblib.dump(model, "model/model.pkl")
    joblib.dump(vectorizer, "model/vectorizer.pkl")
    print("✅ Modelo y vectorizador guardados")

if __name__ == "__main__":
    train_model()
