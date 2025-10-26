# Simple rule-based chatbot
import re

RULES = [
    (r"\b(hi|hello|hey)\b", "Hello! I'm your AI buddy 🤖"),
    (r"who are you", "I'm a simple Python chatbot."),
    (r"how are you", "Doing great! How can I help you today?"),
    (r"(bye|goodbye)", "Bye! Have a great day!"),
]

def respond(msg: str) -> str:
    text = msg.lower().strip()
    for pattern, reply in RULES:
        if re.search(pattern, text):
            return reply
    return "I didn't get that. Try asking about me, or say hi!"

if __name__ == "__main__":
    print("RuleBot ready! Type 'bye' to exit.")
    while True:
        user = input("You: ")
        if user.lower().strip() in {"bye", "goodbye"}:
            print("Bot: Bye! 👋")
            break
        print("Bot:", respond(user))
