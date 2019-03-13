from flask import Flask, render_template, request

unames = ["adam", "colin", "austin", "nick", "ben", "ti", "reggie"]
pwords = {"adam": "muda", "colin": "cman", "austin": "ajs", "nick": "gay", "ben": "anthem", "ti": "kitkat", "reggie": "loser"}

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    global unames
    global pwords
    uname = request.form['uname']
    pword = request.form['pword']
    if uname in unames:
        if uname in pwords.keys():
            if pwords[uname] == pword:
                return render_template('home.html', value="LOGIN SUCCESS")
    return render_template('login.html', value="Login Failed")

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/transaction')
def transaction():
    return render_template('transaction.html')

@app.route('/viewTransactions')
def viewTransactions():
    return render_template('viewTransactions.html')

@app.route('/monthReview')
def monthReview():
    return render_template('monthReview.html')

@app.route('/login')
def logout():
    return render_template('login.html')

#
# HEX: #d5f4e6
#
# HEX: #80ced6
#
# HEX: #fefbd8
#
# HEX: #618685



app.run('127.0.0.1', debug=True)