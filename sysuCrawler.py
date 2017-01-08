# coding=utf-8
from flask import *
import os
import crawler
app = Flask(__name__)


@app.route("/login", methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if crawler.loginSuccess(request.form['username'], request.form['password']):
            session['username'] = request.form['username']
            session['passwrod'] = request.form['password']

            return redirect(url_for('score'))
        else:
            error = u"您的NetID或密码有误，请重新输入"
    return render_template('login.html', error=error)
# set the secret key.  keep this really secret:
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

@app.route("/")
def index():
    # return crawler.getStdConfirmInfo()
    return redirect(url_for('login'))

@app.route("/lesson")
def lesson():
    body = crawler.getLessons()
    print (body.text)
    return render_template('lesson.html', username=session['username'])

@app.route("/score")
def score():
    return render_template('score.html',username=session['username'])

@app.route("/stdInfo")
def stdInfo():
    return render_template('stdInfo.html',username=session['username'])

@app.route("/selectLesson")
def selectLesson():
    body = crawler.getSelectLessons()
    return render_template('selectLesson.html',username=session['username'])

@app.route("/logout")
def logout():
    session.pop('username', None)
    session.pop('password', None)
    return redirect(url_for('login'))

@app.route('/api/scoreDetail', methods=['POST', 'GET'])
def scoreDetail():
    body = crawler.getScore()
    return str(body.table.encode('utf-8'))

@app.route('/api/lessonDetail', methods=['POST', 'GET'])
def lessonDetail():
    body = crawler.getLessons()
    print ('body.table',body.table)
    return str(body.table.encode('utf-8'))

@app.route('/api/stdInfoDetail', methods=['POST', 'GET'])
def stdInfoDetail():
    body = crawler.getStdConfirmInfo()
    return str(body[0])

@app.route('/api/selectLessonDetail', methods=['POST', 'GET'])
def selectLessonDetail():
    body = crawler.getSelectLessons()
    return str(body[0])

if __name__ == "__main__":
    app.run(debug=True)

