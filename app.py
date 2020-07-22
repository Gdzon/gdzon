import os, re
from sqlalchemy import text
from models import Books, db
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
        return "gdz"    # render_template('.html', title=title, grade=grade, subject=subject)
    else:
        abort(404)


if __name__ == '__main__':
    app.run(debug=True)



subjects = ["matematika", "russkij_yazik"]