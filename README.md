# Password-Generator
🔐 Password Generator (Tkinter)

A simple desktop password generator and saver built with Python and Tkinter.
The app generates secure random passwords and stores them locally in a text file.

This project was built as a learning exercise to practice:

Python fundamentals

Tkinter GUI development

Basic OOP structure

File handling

Randomized password generation

✨ Features

Generate strong random passwords using:

Uppercase & lowercase letters

Numbers

Symbols

Save credentials (website, email/username, password) to a local file

Input validation with popup warnings

Simple and clean GUI using Tkinter

🖥️ Tech Stack

Python 3

Tkinter (GUI)

random module

File I/O (.txt storage)

📸 Preview

(Optional: you can add a screenshot here later)

🚀 How to Run

Clone the repository:

git clone https://github.com/your-username/password-generator.git


Navigate into the project folder:

cd password-generator


Run the application:

python main.py


Make sure logo.png is in the same directory as the script.

📂 File Structure
password-generator/
│
├── main.py        # Main application file
├── logo.png       # App logo
├── file.txt       # Saved passwords (created automatically)
└── README.md

🔐 Password Generation Logic

Password length is randomized within defined ranges

Characters are selected randomly from predefined sets

Characters are shuffled to ensure randomness

Final password is assembled into a single string

📝 Notes

Passwords are stored locally in plain text (file.txt)

This project is for learning purposes and not intended for production use

Future improvements could include:

JSON storage

Search functionality

Password length controls

Encryption

UI polish

📚 What I Learned

Structuring a small project using OOP

Managing GUI state with StringVar

Handling user input validation

Writing and appending to files

Improving code readability through refactoring

🤝 Acknowledgments

Built as part of my personal learning journey in Python and software development.
