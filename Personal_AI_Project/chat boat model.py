from PyQt5.QtWidgets import *
import sys
from datetime import datetime
from io import StringIO
import contextlib

def on_clicked(msg):
    message = QMessageBox()
    message.setText(msg)
    message.exec_()

def ghost_chatbot(user_input):
    def calculate_age(birthdate):
        current_date = datetime(2023, 8, 9)  # Current date (update as needed)
        birthdate_with_current_year = birthdate.replace(year=current_date.year)

        if current_date < datetime.combine(birthdate_with_current_year, datetime.min.time()):
            age = current_date.year - birthdate.year - 1
        else:
            age = current_date.year - birthdate.year

        return age

    responses = []

    def respond(response):
        responses.append(response)

    creation_date = datetime(2023, 8, 1)  # Update the creation date as needed

    if "how old am i" in user_input or "calculate age" in user_input or "age calculation" in user_input or "help me to calculate age" in user_input:
        birthdate_input = input("Please enter your birthdate (MM-DD-YYYY): ")
        try:
            birthdate = datetime.strptime(birthdate_input, "%m-%d-%Y").date()
            age = calculate_age(birthdate)
            respond("You are " + str(age) + " years old.")
        except ValueError:
            respond("Invalid date format. Please enter your birthdate in MM-DD-YYYY format.")
    elif user_input.startswith(("hello", "hi", "hey")):
        respond("Hi, I am Ghost. How may I assist you?")
    elif "how are you" in user_input:
        respond("Hey, I am just a computer, always fine.")
    elif "how old are you" in user_input or "your age" in user_input:
        age = calculate_age(creation_date)
        respond("I am " + str(age) + " years old.")
    elif "what is your name" in user_input or "your name" in user_input:
        respond("I am Ghost. How may I help you?")
    elif "bye" in user_input or "exit" in user_input or "close" in user_input:
        respond("See you soon!")
        sys.exit(0)  # Exit the application
    elif any(keyword in user_input for keyword in ["thanks", "thank you", "ok", "see you"]):
        respond("You are welcome. Is there anything else I can help you with?")
    elif "version" in user_input or "your version" in user_input:
        respond("version: 0.01")
    elif "tell me a joke" in user_input:
        respond("Why don't scientists trust atoms? Because they make up everything!")
    elif "weather" in user_input:
        respond("I'm sorry, I don't have access to real-time data. Please check a weather website.")
    elif "help" in user_input:
        respond("Sure! I can assist you with general inquiries, jokes, and more. Feel free to ask!")
    else:
        respond("I am sorry, I couldn't understand. Please ask me again.")

    return '\n'.join(responses)

def main():
    app = QApplication(sys.argv)
    window = QWidget()
    window.setGeometry(100, 100, 400, 400)
    window.setWindowTitle("Ghost Chatbot")

    layout = QVBoxLayout()
    label = QLabel("Ghost Chatbot")
    textbox = QTextEdit()
    button = QPushButton("Send")
    output_box = QTextEdit()  # To display chatbot responses

    def button_clicked():
        user_input = textbox.toPlainText().lower()

        # Call the modified ghost_chatbot function and capture its output
        ghost_chatbot_response = ghost_chatbot(user_input)

        output_box.append("you: " + user_input)
        output_box.append("Ghost: " + ghost_chatbot_response)

    button.clicked.connect(button_clicked)

    layout.addWidget(label)
    layout.addWidget(textbox)
    layout.addWidget(button)
    layout.addWidget(output_box)
    window.setLayout(layout)

    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
