
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle

data = {
    "text": ["hi", "hello", "where is my order", "track my order", "refund policy", "bye"],
    "intent": ["greeting", "greeting", "order_status", "order_status", "refund", "goodbye"]
}

df = pd.DataFrame(data)

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["text"])
y = df["intent"]

model = LogisticRegression()
model.fit(X, y)

pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

print("Model trained and saved")
