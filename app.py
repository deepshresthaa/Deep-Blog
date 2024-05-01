from flask import Flask,render_template,request
from db import Database
app=Flask(__name__)
dbo=Database()


@app.route('/')
def index():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template("register.html")

@app.route('/perform_registration',methods=['post'])
def perform_registration():
    name=request.form.get('users_name')
    email=request.form.get('users_email')
    password=request.form.get("users_password")
    response=dbo.insert(name,email,password)
    if response:
        return render_template('login.html',message='Registered Successfully!')
    else:
        return render_template("register.html",message='User already exists!')
    
@app.route('/perform_login',methods=['post'])
def perform_login():
    email=request.form.get("users_email")
    password=request.form.get("users_password")
    response=dbo.search(email,password)
    if response==1:
        return render_template('index.html')
    elif response==0:
        return render_template('login.html',warning='email/password is incorrect.')
    else:
        return render_template('login.html',warning='Please register first.')


app.run(debug=True)