MakeACharQuiz
Developers: Stephen Lee, Armando Lopez, Jose Sanrindo

Description:
Users can create their own "Which Character Are You Quiz".
They can either choose to create their own quiz or play a quiz.

How to Create a Quiz:
User will be prompted to fill out forms to create a quiz.
Quiz will have exactly 4 characters.
Quiz can have as many questions as the user desires.
Quiz will have exactly 4 options per question.

How to Take a Quiz:
User will click on a quiz from a list of created quizzes.
The clicked link will show the quiz.
Once submitted, the results will show.

Database:
For our project, we will be using sqlite3 as our database.
The database will consist of one table: quiz.
Quiz has the following attributes:
quiz id
quiz title
quiz characters (array size 4)
quiz questions (array)
quiz options (array size 4 x number of questions)

Note:
MySQL and sqlite does not have arrays. Therefore,
it will be stored as a TEXT separated by commas.
The data will need to be parsed to be used.
The database is stored as a database file.
In order to view the database, you can use DB Browser.


Installation Requirements:
Flask
Python
sqlite3
(optional) DB Browser

How to Run the Project
In order to create a new database, delete the quiz.db file and then run "python db.py" in the command prompt.
A quiz.db file should be created.
In order to start the project, type "python main.py" in the command prompt.
Go to http://localhost:5000/ on your web browser and it should open the home page.

File Directory: (type tree {folder path} \f in command prompt)
│   db.py
│   main.py
│   README.md
│
├───static
│   ├───images
│   │       temp.jpg
│   │
│   └───styles
│           homeStyles.css
│           quizResults.css
│           quizTake.css
│
└───templates
        homePage.html
        question_form.html
        quizResults.html
        quizTake.html
        quiz_form.html