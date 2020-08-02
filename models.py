from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(session_options={"autoflush": False})


class Books(db.Model):
    id_ = db.Column(db.String, primary_key=True)
    title = db.Column(db.String)
    subject = db.Column(db.String)
    grade = db.Column(db.Integer)
    cover = db.Column(db.String)
    tasks = db.Column(db.String)
    author = db.Column(db.String)

    def __reps__(self):
        f"<Books {self.id}>"


def addBook(id_, title, subject, grade, cover, tasks, author):
    try:
        b = Books(id_=id_, title=title, subject=subject, grade=grade, cover=cover, tasks=tasks, author=author)
        db.session.add(b)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print("Ошибка добавления в БД: ", str(e))