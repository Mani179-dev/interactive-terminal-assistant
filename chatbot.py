import json
import os
import re

DATASET_FILE = "sample_faq.json"

#1. Load FAQ dataset

def load_faq():

    if not os.path.exists(DATASET_FILE):
        print("Error: FAQ dataset not found!")
        return None

    try:
        with open(DATASET_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data.get("greetings"), list):
            raise ValueError("Invalid greetings format.")

        if not isinstance(data.get("faqs"), list):
            raise ValueError("Invalid FAQ format.")

        for faq in data["faqs"]:
            if not isinstance(faq, dict):
                raise ValueError("Invalid FAQ entry.")

            if "question" not in faq or "answer" not in faq:
                raise ValueError("FAQ entry must contain question and answer.")

        print("FAQ dataset loaded successfully!")
        return data

    except (json.JSONDecodeError, OSError, ValueError) as error:
        print("Error loading dataset:", error)
        return None

#2. Normalize user input

def normalize_input(user_input):
    return user_input.lower().strip()

#3. Check greeting

def check_greeting(user_input, greetings):

    message = normalize_input(user_input)

    for greeting in greetings:
        pattern = r"\b" + re.escape(greeting.lower()) + r"\b"

        if re.search(pattern, message):
            return True

    return False

#4. Identify multiple FAQ intents

def find_faqs(user_input, faqs):

    message = normalize_input(user_input)

    intent_patterns = {
    "hours": r"\b(hours?|timing|open|close|operation)\b",
    "project": r"\b(internship|project|submit|submission)\b",
    "certificate": r"\b(certificate|certificates|certification)\b"}

    matched_answers = []

    for index, (intent, pattern) in enumerate(intent_patterns.items()):

        if re.search(pattern, message):
            if index < len(faqs):
                matched_answers.append(faqs[index]["answer"])

    return matched_answers

#5. Generate chatbot response

def get_response(user_input, data):

    message = normalize_input(user_input)

    if not message:
        return "Please enter a question."

    if message in ["bye", "exit", "quit"]:
        return "EXIT"

    responses = []

# Greeting recognition
    if check_greeting(message, data["greetings"]):
        responses.append("Hello! Welcome. How can I help you?")
    

# FAQ recognition
    answers = find_faqs(message, data["faqs"])
    responses.extend(answers)

    if responses:
        return "\n".join(responses)

    return ("Sorry, I couldn't understand your question.\n"
        "Please ask about working hours, projects or certificates."
    )
    

#6. Main chatbot function

def main():

    data = load_faq()

    if data is None:
        return

    print("\n======================================")
    print("     DATHEON INTERACTIVE CHATBOT")     
    print("===========================================")
    print("you can ask me about:")
    print("1.Business Working hours")
    print("2.internship project submission")
    print("Certificate information")  
      
    print("\nType 'bye', 'exit' or 'quit' to stop.")
    print("--------------------------------------") 

    while True:

        try:
            user_input = input("\nYou: ")

            response = get_response(user_input, data)

            if response == "EXIT":
                print("\nBot: Thank you for chatting!")
                print("Bot: Goodbye!")
                break

            print("\nBot:", response)

        except (EOFError, KeyboardInterrupt):
            print("\n\nBot: Chat ended. Goodbye!")
            break

        except Exception as error:
            print("\nBot: Something went wrong.")
            print("Please try again.")
            print("Error:", error)

#7. Program execution

if __name__ == "__main__":
   main()