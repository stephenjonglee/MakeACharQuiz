from flask import *
import sqlite3, hashlib, os
from werkzeug.utils import secure_filename

app = Flask(__name__)

# display home page
@app.route('/')
def home_page():
    return render_template("homePage.html")

# display question form
@app.route('/question_form.html', methods = ['GET', 'POST'])
def question_form():
    if request.method == 'POST':
        #Parse form data    
        question = request.form['question'] + " | "
        optionA = request.form['optionA']
        optionB = request.form['optionB']
        optionC = request.form['optionC']
        optionD = request.form['optionD']

        optArray = optionA + ", " + optionB + ", " + optionC + ", " + optionD + " | "

        with sqlite3.connect('quiz.db') as con:
            try:
                cur = con.cursor()

                # update last row
                sql = ''' UPDATE quiz 
                SET qArray = qArray || ?, 
                optionArray = optionArray || ? 
                WHERE quizId = (SELECT MAX(quizId) FROM quiz)'''
                cur.execute(sql, (question, optArray))
                con.commit()
            except:
                con.rollback()
        con.close()

        # if the next question button is clicked
        if request.form['submit_btn'] == 'nxt':
            return redirect(url_for("question_form"))
        
        # if the submit button is clicked
        elif request.form['submit_btn'] == 'done':
            return redirect(url_for("home_page"))    
    
    return render_template("question_form.html")

# display quiz form
@app.route('/quiz_form.html', methods = ['GET', 'POST'])
def quiz_form():
    if request.method == 'POST':
        # Parse form data    
        title = request.form['title']
        charA = request.form['charA']
        charB = request.form['charB']
        charC = request.form['charC']
        charD = request.form['charD']

        charArray = charA + ', ' + charB + ', ' + charC + ', ' + charD

        with sqlite3.connect('quiz.db') as con:
            cur = con.cursor()
            sql = ''' INSERT INTO quiz (title, charArray, qArray, optionArray) 
            VALUES (?, ?, "", "")'''
            cur.execute(sql, (title, charArray))
            con.commit()
        con.close()

        return redirect(url_for("question_form"))

    return render_template("quiz_form.html")

# display quiz results
@app.route('/quizResults.html')
def quiz_result():
    return render_template("quizResults.html")

# display quiz take
@app.route('/quizTake.html')
def quiz_take():

    # retrieve data from database
    with sqlite3.connect('quiz.db') as con:
        cur = con.cursor()
        sql = ''' SELECT *
        FROM quiz
        WHERE quizId = (SELECT MAX(quizId) FROM quiz)'''
        cur.execute(sql)
        record = cur.fetchall()[0]
    con.close()

    title = record[1]
    qArray = record[3]
    optionArray = record[4]

    # data text needs to be parsed into an array
    questions = qArray.split(" | ")
    num = len(questions) - 1
    # # split options in groups of 4
    options = []
    opts = optionArray.split(' | ')
    temp = ""
    for i in range(0, num):
        temp = opts[i].split(", ")
        options.append(temp)

    return render_template("quizTake.html", title = "title", questions = questions, options = options, num = num)

if __name__ == '__main__':
    app.run(debug=True)