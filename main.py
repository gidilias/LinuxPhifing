import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib

df = pd.read_csv("data/phishing_data.csv")

safe = pd.DataFrame({
    "domain": ["google.com", "yandex.kz", "github.com", "facebook.com"],
    "label": ["Safe"] * 4
})

df = pd.concat([df, safe], ignore_index=True)

X_raw = df["domain"]
y = df["label"]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(X_raw)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

print("CLassification result")
print(classification_report(y_test, model.predict(X_test)))

joblib.dump(model, "model.joblib")
joblib.dump(vectorizer, "vectorizer.joblib")

while True:
    url = input("\nURL ").strip()
    if url.lower() == "exit":
        break
    features = vectorizer.transform([url])
    prediction = model.predict(features)[0]
    print(f"Result: {prediction}")