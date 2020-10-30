import sqlite3

#Open database
conn = sqlite3.connect('quiz.db')

#Create table
conn.execute('''CREATE TABLE quiz 
		(quizId INTEGER PRIMARY KEY, 
		title TEXT,
		charArray TEXT,
		qArray TEXT,
		optionArray TEXT
		)''')

conn.close()