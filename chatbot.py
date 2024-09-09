import spacy
import random

nlp = spacy.load('en_core_web_sm')

responses = {
    "greet": ["Hello!", "Hi there!", "Hey!", "Greetings!"],
    "bye": ["Goodbye!", "See you later!", "Bye!"],
    "name": ["I'm a chatbot created using spaCy.", "You can call me ChatBot!"],
    "howareyou": ["I'm just a program, but thanks for asking! How can I help you?"],
    "default": ["I'm sorry, I don't understand that."]
}

def respond_to_user(message):
    doc = nlp(message.lower())

    if any([token.text in ["hi", "hello", "hey", "greetings"] for token in doc]):
        return random.choice(responses["greet"])
    
    elif any([token.text in ["bye", "goodbye", "see you"] for token in doc]):
        return random.choice(responses["bye"])
    
    elif any([token.lemma_ in ["name", "who", "what"] for token in doc]):
        if "name" in message:
            return random.choice(responses["name"])

    elif "how" in message and "you" in message:
        return random.choice(responses["howareyou"])

    return random.choice(responses["default"])

def chatbot():
    print("ChatBot: Hello! How can I assist you today?")
    while True:
        message = input("You: ")
        if "bye" in message.lower():
            print("ChatBot:", respond_to_user(message))
            break
        else:
            print("ChatBot:", respond_to_user(message))

if __name__ == "__main__":
    chatbot()
