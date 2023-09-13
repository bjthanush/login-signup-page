from flask import Flask, render_template,flash, redirect,url_for,session,logging,request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/project1'
db = SQLAlchemy(app)

class userdata(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    email = db.Column(db.String(120))
    password = db.Column(db.String(80))

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/login", methods = ['GET', 'POST'])
def login():
    if request.method == "POST":
        mails = request.form["mail"]
        passws = request.form["passw"]
        
        login = userdata.query.filter_by(email=mails, password=passws).first()
        if login is not None:
            return redirect(url_for("soutput"))
        else:
            return redirect(url_for("foutput"))
    return render_template("login.html")

@app.route("/signup", methods = ['GET', 'POST'])
def singup():
    if request.method == "POST":
        unames = request.form['uname']
        mails = request.form['email']
        passws = request.form['passw']

        register = userdata(username = unames, email = mails, password = passws)
        db.session.add(register)
        db.session.commit()

        return redirect(url_for("login"))
    return render_template("signup.html")

@app.route("/dataset")
def dataset():
    posts = userdata.query.filter_by().all()
    return render_template("dataset.html",posts=posts)

@app.route("/soutput")
def soutput():
    return render_template("output.html", message = "successfully")

@app.route('/foutput')
def foutput():
    return render_template("output.html", message = "un-successfully")


if __name__=='__main__':
    app.run(debug=True)