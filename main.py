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
        # if the next question button is clicked
        if request.form['submit_btn'] == 'nxt':
            #Parse form data    
            question = request.form['question']
            optionA = request.form['optionA']
            optionB = request.form['optionB']
            optionC = request.form['optionC']
            optionD = request.form['optionD']

            optArray = optionA + ", " + optionB + ", " + optionC + ", " + optionD

            with sqlite3.connect('quiz.db') as con:
                try:
                    cur = con.cursor()
                    # retrieving data from last row
                    sql = ''' SELECT qArray FROM quiz ORDER BY quizId DESC LIMIT 1 '''
                    qArray = cur.execute(sql)
                    sql = ''' SELECT optionArray FROM quiz ORDER BY quizId DESC LIMIT 1 '''
                    optionArray = cur.execute(sql)

                    # add question and options to arrays
                    qArray = qArray + ", " + question
                    optionArray = optionArray + ", " + optArray

                    # update last row
                    sql = ''' UPDATE quiz
                        SET qArray = ?,
                            optionArray = ?
                        WHERE quizId = (SELECT MAX(quizID) FROM quiz)'''
                    cur.execute(sql, (qArray, optionArray))
                    con.commit()
                except:
                    con.rollback()
            con.close()

            return redirect(url_for("question_form"))
        
        # if the submit button is clicked
        elif request.form['submit_btn'] == 'done':
            #Parse form data    
            question = request.form['question']
            optionA = request.form['optionA']
            optionB = request.form['optionB']
            optionC = request.form['optionC']
            optionD = request.form['optionD']

            optionArray = optionA + ", " + optionB + ", " + optionC + ", " + optionD

            with sqlite3.connect('quiz.db') as con:
                try:
                    cur = con.cursor()
                    # retrieving data from last row
                    sql = ''' SELECT qArray FROM quiz ORDER BY quizId DESC LIMIT 1 '''
                    qArray = cur.execute(sql)
                    sql = ''' SELECT optionArray FROM quiz ORDER BY quizId DESC LIMIT 1 '''
                    optionArray = cur.execute(sql)

                    # add question and options to arrays
                    qArray = qArray + ", " + question
                    optionArray = optionArray + ", " + optArray

                    # update last row
                    sql = ''' UPDATE quiz
                        SET qArray = ?,
                            optionArray = ?
                        WHERE quizId = (SELECT MAX(quizID) FROM quiz)'''
                    cur.execute(sql, (qArray, optionArray))
                    con.commit()
                except:
                    con.rollback()
            con.close()

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
        
        qArray = ''
        optionArray = ''

        with sqlite3.connect('quiz.db') as con:
            cur = con.cursor()
            sql = ''' INSERT INTO quiz (title, charArray, qArray, optionArray)
                VALUES (?, ?, ?, ?)'''
            cur.execute(sql, (title, charArray, qArray, optionArray))
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
    return render_template("quizTake.html")

# # def getQuizDetails():
# #     with sqlite3.connect('quiz.db') as conn:
# #         cur = conn.cursor()
# #         loggedIn = True
# #         cur.execute("SELECT userId, firstName FROM users WHERE email = '" + session['email'] + "'")
# #         userId, firstName = cur.fetchone()
# #         cur.execute("SELECT count(productId) FROM kart WHERE userId = " + str(userId))
# #         noOfItems = cur.fetchone()[0]
# #     conn.close()
# #     return (loggedIn, firstName, noOfItems)

# @app.route("/registerationForm")
# def registrationForm():
#     return render_template("register.html")

# def allowed_file(filename):
#     return '.' in filename and \
#             filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

# def parse(data):
#     ans = []
#     i = 0
#     while i < len(data):
#         curr = []
#         for j in range(7):
#             if i >= len(data):
#                 break
#             curr.append(data[i])
#             i += 1
#         ans.append(curr)
#     return ans

if __name__ == '__main__':
    app.run(debug=True)