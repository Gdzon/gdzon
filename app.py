import os, re
from sqlalchemy import text
from models import Books, db, addBook
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, url_for, request, session, g, redirect, abort, flash
from flask_navigation import Navigation

# config

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///first.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'wefhiu42h5ui43h534uth3u4itbger'
db.init_app(app)
THIS_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)))


# app.ROUTE decorators

@app.context_processor
def base_vars():
    return dict(subjects=subjects, Books=Books)


@app.route('/')
def index():
    # db.drop_all()
    # db.create_all()
    return render_template('index.html', title="hello!", subjects=subjects, page_title="GDZon", grade=0)


@app.route('/<grade>/<subject>/<book>/<int:task>')
def show_task(grade, subject, book, task):
    tasks = os.listdir(os.path.join(THIS_FOLDER, r'static/img/tasks/' + book))
    tasks = sorted(tasks, key=lambda x: int("".join([i for i in x if i.isdigit()])))
    if re.match(r"\d[0,1]?-klass", grade) and subject in subjects.keys():
        try:
            book_info = Books.query.filter_by(id_=book).first()
            if book_info:
                return render_template('task.html',
                                       page_title=f"Задание {task}.  {book_info.author}.  {subjects[subject][-1]}:  "
                                                  f"{grade[:-6]}  класс",
                                       task_num=task,
                                       url=f'/{grade}/{subject}/{book}',
                                       book_author=book_info.author,
                                       book_id=book_info.id_,
                                       grade=grade[:-6],
                                       subject=subjects[subject][-1],
                                       len=len(tasks),
                                       tasks=tasks
                                       )

        except Exception as e:
            print("Ошибка загрузки задания: " + str(e))

    else:
        abort(404)


@app.route('/<grade>/<subject>/<book>')
def book_tasks(grade, subject, book):
    tasks = os.listdir(os.path.join(THIS_FOLDER, r'static/img/tasks/' + book))
    tasks = sorted(tasks, key=lambda x: int("".join([i for i in x if i.isdigit()])))
    if re.match(r"\d[0,1]?-klass", grade) and subject in subjects.keys():
        try:
            book_info = Books.query.filter_by(id_=book).first()

            if book_info:
                print([book_info.grade])
                book_info.grade = str(book_info.grade)
                return render_template('bookTasks.html',
                                       page_title=f"{book_info.author}. {subjects[subject][-1]}: {grade[:-6]} класс",
                                       book_info=book_info,
                                       url=f'/{grade}/{subject}/{book}',
                                       book=book_info.author,
                                       grade=grade[:-6],
                                       subject=subjects[subject][-1],
                                       len=len(tasks)
                                       )
            else:
                abort(404)

        except Exception as e:
            print("Ошибка получения книги: " + str(e))

    else:
        abort(404)


@app.route("/<grade>/<subject>")
def table_to_books(grade, subject):
    if re.match(r"\d[0,1]?-klass", grade) and subject in subjects.keys():
        try:
            grade = str(grade[:len(grade) - 6])
            books_list = Books.query.filter_by(grade=grade, subject=subject).all()
            return render_template('booksList.html',
                                   page_title=f"{subjects[subject][-1]}: {grade} класс",
                                   books_list=books_list,
                                   grade=grade,
                                   subject=subject,
                                   ru_subject=subjects[subject][-1],
                                   url=f'/{str(grade) + "-klass"}/{subject}',
                                   )
        except Exception as e:
            print("Ошибка получения списка книг: ", str(e))
    else:
        abort(404)


@app.route("/search", methods=['GET'])
def search():
    pass


@app.route('/admin', methods=['POST', 'GET'])
def admin():
    if request.method == 'POST':
        if len(request.form['address']) > 0:
            flash('Сообщение отправлено', category='success')
        else:
            flash('Ошибка отправки', category='error')

    return render_template("admin.html", page_title="Админка")


subjects = {"Класс": ["Класс"],
            "maths": ["Математика"], "algebra": ["Алгебра"],
            "geometries": ["Геометрия"], "english": ["Английский"],
            "nemeckiy": ["Немецкий"], "phisic": ["Физика"],
            "him": ["Химия"], "biolog": ["Биология"],
            "geography": ["География"], "history": ["История"],
            "information": ["Информатика"], "literature": ["Литература"]}

if __name__ == '__main__':
    app.run(debug=True)
