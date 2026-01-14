import pandas as pd
import nltk

from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

nltk.download("punkt")
with open("stop-words-list.txt", "r", encoding="latin-1") as f:
    stop_words = set(f.read().splitlines())


trainingfile = pd.read_csv("train.csv", encoding="latin-1")
testfile = pd.read_csv("test.csv", encoding="latin-1")


trainingfile = trainingfile[["text", "sentiment"]].dropna()
testfile = testfile[["text", "sentiment"]].dropna()

trainingfile["sentiment"] = trainingfile["sentiment"].astype(str)
testfile["sentiment"] = testfile["sentiment"].astype(str)


def preprocess(text):
    text = str(text).lower()
    cleaned_chars = []
    for c in text:
        if c.isalpha() or c.isspace():
            cleaned_chars.append(c)
    text = "".join(cleaned_chars)
    tokens = word_tokenize(text)
    filtered_tokens = []
    for t in tokens:
        if t not in stop_words:
            filtered_tokens.append(t)
    return " ".join(filtered_tokens)


trainingfile["clean_tweet"] = trainingfile["text"].apply(preprocess)
testfile["clean_tweet"] = testfile["text"].apply(preprocess)

unique_words = set()
for tweet in trainingfile["clean_tweet"]:
    unique_words.update(tweet.split())

vectorizer = TfidfVectorizer()
X_train = vectorizer.fit_transform(trainingfile["clean_tweet"])
X_test = vectorizer.transform(testfile["clean_tweet"])

Y_train = trainingfile["sentiment"]
Y_test = testfile["sentiment"]

model = LogisticRegression(max_iter=1000)
model.fit(X_train, Y_train)

Y_pred = model.predict(X_test)

print("Unique Words Count:", len(unique_words))
print("Accuracy:", accuracy_score(Y_test, Y_pred))
print(classification_report(Y_test, Y_pred))
print(confusion_matrix(Y_test, Y_pred))
