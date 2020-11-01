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
    
    else:
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

    else:
        return render_template("quiz_form.html")

# display quiz list
@app.route('/quizList.html', methods = ['GET', 'POST'])
def quiz_list():
    if request.method == 'POST':
        # Parse form data
        index = request.form['index']

        return redirect(url_for("quiz_take", pindex = index))

    else:
        #retrieve data
        with sqlite3.connect('quiz.db') as con:
            cur = con.cursor()
            sql = ''' SELECT title
            FROM quiz'''
            cur.execute(sql)
            record = cur.fetchall()
        con.close()

        # parsing data
        quizzes = [i[0] for i in record]

        # number of quizzes in database
        num = len(quizzes)

        return render_template("quizList.html", quizzes = quizzes, num = num)

# display quiz take
@app.route('/quizTake.html', methods = ['GET', 'POST'])
def quiz_take():
    if request.method == 'POST':
        # request parameter index
        index = request.args['pindex']

        # retrieve data from database
        with sqlite3.connect('quiz.db') as con:
            cur = con.cursor()
            sql = ''' SELECT *
            FROM quiz
            WHERE quizId = ?'''
            cur.execute(sql, index)
            record = cur.fetchall()[0]
        con.close()

        charArray = record[2]
        qArray = record[3]

        # data text needs to be parsed into an array
        questions = qArray.split(" | ")
        num = len(questions) - 1
        characters = charArray.split(", ")

        # tally variable
        tally = [0, 0, 0, 0]

        # parse form data
        # updates the tally
        for i in range(0, num):
            name = 'option' + str(i)
            option = request.form[name]
            if option == "0":
                tally[0] = tally[0] + 1
            elif option == "1":
                tally[1] = tally[1] + 1
            elif option == "2":
                tally[2] = tally[2] + 1
            elif option == "4":
                tally[4] = tally[4] + 1
        
        # find largest tally and it's position
        max_value = max(tally)
        max_index = tally.index(max_value)

        # get character from index
        character = characters[max_index]

        return redirect(url_for("quiz_result", pcharacter = character))

    else:
        # request parameter index
        index = request.args['pindex']

        # retrieve data from database
        with sqlite3.connect('quiz.db') as con:
            cur = con.cursor()
            sql = ''' SELECT *
            FROM quiz
            WHERE quizId = ?'''
            cur.execute(sql, index)
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

        return render_template("quizTake.html", title = title, questions = questions, options = options, num = num)

# display quiz results
@app.route('/quizResults.html')
def quiz_result():
    # get parameter
    character = request.args['pcharacter']
    return render_template("quizResults.html", character = character)

if __name__ == '__main__':
    app.run(debug=True)