from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(session_options={"autoflush": False})


class Books(db.Model):
    books_id = db.Column(db.Integer, primary_key=True)
    grade = db.Column(db.Integer)
    cover = db.Column(db.String)
    tasks = db.Column(db.String)
    author = db.Column(db.String)

    def __reps__(self):
        f"<Books {self.id}>"


def addBook(grade, cover, tasks, author):
    try:
        b = Books(grade=grade, cover=cover, tasks=tasks, author=author)
        db.session.add(b)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print("Ошибка добавления в БД: ", str(e))