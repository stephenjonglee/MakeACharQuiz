MakeACharQuiz
Developers: Stephen Lee, Armando Lopez, Jose Sanrindo

Description:
Users can create their own "Which Character Are You Quiz".
They can either choose to create their own quiz or play a quiz.

Our project is saved under a Github repository: https://github.com/stephenjonglee/MakeACharQuiz

How to Create a Quiz:
User will be prompted to fill out forms to create a quiz.
Quiz will have exactly 4 characters.
Quiz will have exactly 5 questions.
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
Python or Python3
Flask - to install type "pip install flask" in command prompt
SQLite
(optional) DB Browser if you want to look at the database

How to Run the Project
In order to create a new database, delete the quiz.db file and then run "python db.py" in the command prompt.
A quiz.db file should be created.
In order to start the project, type "python main.py" in the command prompt or "python3 main.py" if you are using Python3.
Go to http://localhost:5000/ on your web browser and it should open the home page.

Task Division:
Tasks were divided up into three main parts:
Front-end HTML Forms (creating a quiz) assigned to Jose Sanrindo
Front-end HTML Templates (playing a quiz) assigned to Armando Lopez
Back-end Python/Flask (connects and modifies the database) assigned to Stephen Lee

Other tasks include making home page, testing the html files, testing python, and testing database.
We use Trello to list our tasks and assignments: https://trello.com/b/xz9cHKUp/group-project-1

Team Meetings:
We used Discord to conduct our team meetings to go over our tasks done, what needs to be done,
what needs to be modified, and what would be nice to include.
We share screen to review our coding and testing together.

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