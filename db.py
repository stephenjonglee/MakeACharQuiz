import sqlite3

#Open database
conn = sqlite3.connect('quiz.db')

#Create table quiz
# Attributes: title, array of characters, array of questions, and array of options
conn.execute('''CREATE TABLE quiz
     (quizId INTEGER PRIMARY KEY AUTOINCREMENT,
     title TEXT,
     charArray TEXT,
     qArray TEXT,
     optionArray TEXT)
     ''')

conn.close()