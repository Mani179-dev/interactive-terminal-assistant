Interactive Terminal Assistant / Chatbot

Project Overview

The Interactive Terminal Assistant is a rule-based chatbot developed using Python. It recognizes greetings, identifies user queries using keywords and regular expressions, and provides contextual responses using a JSON FAQ dataset.

Features

- Greeting recognition
- FAQ-based question answering
- Multi-intent recognition
- Keyword matching using Regular Expressions
- JSON dataset integration
- Continuous conversation
- Fallback responses for unknown questions
- Exit commands (bye, exit, quit)
- Error handling

Technologies Used

- Python 3
- JSON
- Regular Expressions (re)
- OS module

Project Structure

interactive-terminal-assistant/
│
├── chatbot.py
├── sample_faq.json
└── README.md

How to Run

1. Install Python 3.
2. Download or clone this repository.
3. Open the project folder in VS Code.
4. Open the terminal.
5. Run the following command:

python chatbot.py

Sample Conversation

You: hello

Bot: Hello! Welcome. How can I help you?

You: What are your working hours?

Bot: We operate Monday through Friday from 9:00 AM to 6:00 PM IST.

You: bye

Bot: Thank you for chatting!
Bot: Goodbye!

Learning Outcomes

- Understanding Python functions
- Working with JSON files
- Using regular expressions
- Implementing rule-based intent recognition
- Exception handling
- Building interactive terminal applications

Future Improvements

- Add more FAQ categories
- Improve intent recognition
- Develop a graphical user interface
- Integrate a database
- Explore Natural Language Processing (NLP)

Author

Developed as a Python project for Datheon.
