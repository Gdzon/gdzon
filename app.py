# import

import os, re
from sqlalchemy import text
from models import Books, db, addBook
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, url_for, request, session, g, redirect, abort
from flask_navigation import Navigation


# config

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///first.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


# app.ROUTE decorators

@app.route('/')
def index():
    print()
    return render_template('index.html', title="hello!")


@app.route('/<grade>/<subject>/<book>')
def book_tasks(grade, subject, book):
    if re.match(r"\d[0,1]?-klass", grade) and subject in subjects:
        try:
            book_info = Books.query.filter_by(id_=book).first()

            if book_info:
                return render_template('',
                                       page_title=book_info.title,
                                       book_title=book_info.title,
                                       subject=subject,
                                       description=book_info.description,
                                       grade=book_info.grade,
                                       cover=book_info.cover,
                                       tasks=book_info.tasks,
                                       tasks_num=len([elem for elem in os.listdir(book_info.tasks)]),
                                       author=book_info.author)
            else: abort(404)

        except Exception as e:
            print("Ошибка получения книги: ", str(e))

    else: abort(404)


@app.route("/<grade>/<subject>")
def table_to_books(grade, subject):

    if re.match(r"\d[0,1]?-klass", grade) and subject in subjects:
        try:
            books_list = Books.query.filter_by(grade=grade[:len(grade)-6], subject=subject).all()
            return render_template('booksList.html',
                                    page_title=f"Книги {grade} класс {subject}",
                                    books_list=books_list)
        except Exception as e:
            print("Ошибка получения списка книг: ", str(e))
    else:
        abort(404)


#

if __name__ == '__main__':
    app.run(debug=True)


subjects = ["matematika"]