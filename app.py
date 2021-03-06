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
    #db.drop_all()
    #db.create_all()
    #addBook("testidbook", "matematika", "kniga", 5, "Пушкин", "Издательство", "задачник", 1)
    return render_template('index.html', title="hello!", booksExist=booksExist, str_nums=str_nums, page_title="ГДЗон")


@app.route('/<grade>/<subject>/<book>/<int:task>')
def show_task(grade, subject, book, task):
    if re.match(r"\d[0,1]?-klass", grade) and subject in subjects:
        try:
            book_info = Books.query.filter_by(id_=book).first()
            t = book_info.each_task_num.index(f"n{task}")
            task_amount = int(book_info.each_task_num[t+3:t+5])
            if book_info:
                return render_template('task.html',
                                       page_title=f"Задание {task}. {book_info.author}. {booksExist[subject][-1]}: {grade[:-6]} класс",
                                       book_info=book_info,
                                       task_num=task,
                                       task_amount=task_amount)

        except Exception as e:
            print("Ошибка загрузки задания: " + str(e))

    else:
        abort(404)

@app.route('/<grade>/<subject>/<book>')
def book_tasks(grade, subject, book):
    if re.match(r"\d[0,1]?-klass", grade) and subject in subjects:
        try:
            book_info = Books.query.filter_by(id_=book).first()

            if book_info:
                book_info.tasks_count += 1
                book_info.grade = str(book_info.grade)
                return render_template('bookTasks.html',
                                       page_title=f"{book_info.author}. {booksExist[subject][-1]}: {grade[:-6]} класс",
                                       book_info=book_info)
            else: abort(404)

        except Exception as e:
            print("Ошибка получения книги: " + str(e))

    else: abort(404)


@app.route("/<grade>/<subject>")
def table_to_books(grade, subject):

    if re.match(r"\d[0,1]?-klass", grade) and subject in subjects:
        try:
            grade=grade[:len(grade)-6]
            books_list = Books.query.filter_by(grade=grade, subject=subject).all()
            return render_template('booksList.html',
                                    page_title=f"{booksExist[subject][-1]}: {grade} класс",
                                    books_list=books_list,
                                    grade=grade,
                                    subject=subject)
        except Exception as e:
            print("Ошибка получения списка книг: ", str(e))
    else:
        abort(404)

@app.route("/search", methods=['GET'])
def search():
   pass

######

subjects = ["matematika", "russkiy-yazik", "english", "algebra", "geometria", "fizika", "himiya", "nemeckiy_yazik", "biologiya", "geografiya", "istoriya", "informatika", "literatura"]

#for index.html
booksExist = {
    "Класс": ["Класс"],#f  1   2    3    4    5     6    7    8    9    10   11    subj
    "matematika":       ["no","no","no","no","be","no","no","no","no","no","no","Математика"        ],
    "algebra":          ["no","no","no","no","no","no","no","no","no","no","no","Алгебра"           ],
    "geometria":        ["no","no","no","no","no","no","no","no","no","no","no","Геометрия"         ],
    "russkiy-yazik":    ["no","no","no","no","no","no","no","no","no","no","no","Русский язык"      ],
    "english":          ["no","no","no","no","no","no","no","no","no","no","no","Английский язык"   ],
    "nemeckiy_yazik":   ["no","no","no","no","no","no","no","no","no","no","no","Немецкий язык"     ],
    "fizika":           ["no","no","no","no","no","no","no","no","no","no","no","Физика"            ],
    "himiya":           ["no","no","no","no","no","no","no","no","no","no","no","Химия"             ],
    "biologiya":        ["no","no","no","no","no","no","no","no","no","no","no","Биология"          ],
    "geografiya":       ["no","no","no","no","no","no","no","no","no","no","no","География"         ],
    "istoriya":         ["no","no","no","no","no","no","no","no","no","no","no","История"           ],
    "informatika":      ["no","no","no","no","no","no","no","no","no","no","no","Информатика"       ],
    "literatura":       ["no","no","no","no","no","no","no","no","no","no","no","Литература"        ]
}
str_nums = ["0","1","2","3","4","5","6","7","8","9","10","11"]

#

if __name__ == '__main__':
    app.run(debug=True)
