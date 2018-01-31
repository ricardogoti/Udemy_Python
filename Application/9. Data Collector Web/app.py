from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_email import send_email
from sqlalchemy.sql import func

app=Flask(__name__)
#app.config ['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:gundamwing@localhost/height_collector'
#Se agrega ?sslmode=require para poder accesar desde una pc a la base de datos
app.config ['SQLALCHEMY_DATABASE_URI'] = 'postgres://pfigieknrkkeqb:b3fd9f1027a42cc48aee016097619e74a4d28a2ce21b89dcef2ff07f85364010@ec2-54-225-103-255.compute-1.amazonaws.com:5432/d69cg0lmie4v7n?sslmode=require'
db = SQLAlchemy(app)

class Data(db.Model):
    __tablename__ = "data"
    id     = db.Column(db.Integer, primary_key = True)
    email_ = db.Column(db.String(120), unique = True)
    height_ = db.Column(db.Integer)

    def __init__(self, email_, height_):
        self.email_ = email_
        self.height_ = height_

@app.route("/")
def index():
    return render_template("index.html")

#implicitamente son metodos tipo GET
@app.route("/success", methods=['POST'])
def success():
    if request.method == 'POST':
        email  = request.form["email_name"]
        height = request.form ["height_name"]
        if db.session.query(Data).filter(Data.email_==email).count() == 0:
            data = Data(email, height)
            db.session.add(data)
            db.session.commit()
            #Se ejecuta query en la base datos y se le agrega funcion scalar para que solo retorne el valor del query
            average_height = round(db.session.query(func.avg(Data.height_)).scalar(), 2)
            count = db.session.query(Data.height_).count()
            send_email(email, height, average_height, count)
            return render_template("success.html")
    return render_template("index.html",
    text = "Seems like we've got something from that email address already!")

if __name__ == '__main__':
    app.run(debug=True)
