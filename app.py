import os, re
from models import db, Books
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, url_for, request, session, g, redirect, abort

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///first.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


@app.route('/')
def index():
    return "hello!"


@app.route("/<grade>/<subject>")
def table_to_books(grade, subject):
    if re.match(r"\d[0,1]?-klass", grade) and subject in subjects:
        return "hello!"    # render_template('.html', grade=grade, subject=subject)
    else:
        abort(404)


if __name__ == '__main__':
    app.run(debug=True)



subjects = ["matematika", "russkij_yazik"]