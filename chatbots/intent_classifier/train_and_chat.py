
import json
from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

DATA_PATH = Path(__file__).with_name("intents.json")


def load_data():
    data = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    X_text, y = [], []
    for intent, examples in data.items():
        X_text.extend(examples)
        y.extend([intent]*len(examples))
    return X_text, y

def train_model(X_text, y):
    vec = TfidfVectorizer(ngram_range=(1,2))
    X = vec.fit_transform(X_text)
    clf = LogisticRegression(max_iter=1000).fit(X, y)
    return vec, clf

RESPONSES = {
    "greet": "Hello! 👋",
    "about_bot": "I'm a small ML chatbot trained on intents.",
    "help": "Sure—ask me anything about this demo!",
    "goodbye": "Goodbye! 👋"
}

if __name__ == "__main__":
    X_text, y = load_data()
    vec, clf = train_model(X_text, y)

    print("MLChat ready. Type 'exit' to quit.")
    while True:
        msg = input("You: ").strip()
        if msg.lower() == "exit":
            break
        intent = clf.predict(vec.transform([msg]))[0]
        print("Bot:", RESPONSES.get(intent, "Hmm… I’m not sure yet."))

