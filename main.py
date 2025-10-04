from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class Test(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        nutzer = db.Column(db.String(200), nullable=True)
        alter = db.Column(db.Integer)
        geburtstag = db.Column(db.DateTime(), default=datetime.utcnow)

class Users(db.Model):
        email = db.Column(db.String(200), primary_key=True)
        nutzer = db.Column(db.String(200), primary_key=True)
        passwort = db.Column(db.String(200))
        alter = db.Column(db.Integer)
        erstellzeit = db.Column(db.DateTime(), default=datetime.utcnow)


with app.app_context():
    db.create_all()
    
@app.route("/")
def index():
    return render_template("index2.html")

@app.route("/zurueck", methods=['POST'])
def zurueck():
     return redirect("/")

@app.route("/anmelden", methods=['POST'])
def anmelden():
     return render_template("anmeldung.html")

@app.route("/senden", methods=['POST'])
def get_user():
     username_find = request.form['username']
     password = request.form['password']
     user = Users.query.filter_by(nutzer = username_find).first()
     if user.passwort == password:
          return 'Du bist angemeldet!'
     else: 
          return 'Falsche Daten!'



@app.route("/registrieren", methods=['POST'])
def registrieren():
     return render_template("registrieren.html")

@app.route("/save_user", methods=['POST'])
def add_user():
    if request.form['password'] == request.form['password2']: 
        new_entry = Users(
            email = request.form['email'],
            nutzer = request.form['username'],
            passwort = request.form['password'],
            alter = request.form['alter']
        )
        db.session.add(new_entry)
        db.session.commit()
        return render_template("anmeldung.html")

@app.route('/save', methods=['POST'])
def add_input():
    new_entry = Test(
        id = request.form['user_input'],
        nutzer = request.form['user_input2'],
        alter = request.form['user_input3']
    )
    db.session.add(new_entry)
    db.session.commit()
    users = Test.query.order_by(Test.id).all()
    return render_template("save.html")

if __name__ == "__main__":
    app.run(debug=True)