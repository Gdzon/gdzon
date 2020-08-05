from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(session_options={"autoflush": False})


class Books(db.Model):

    id_ = db.Column(db.String, primary_key=True)
    title = db.Column(db.String)
    subject = db.Column(db.String)
    description = db.Column(db.Text)
    grade = db.Column(db.Integer)
    author = db.Column(db.String)
    pub_h = db.Column(db.String)
    type = db.Column(db.String)

    def __reps__(self):
        f"<Books {self.id}>"


def addBook(id_, title, subject, description, grade, author, pub_h):
    try:
        b = Books(id_=id_, title=title, subject=subject, description=description, grade=grade, author=author, pub_h=pub_h)
        db.session.add(b)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print("Ошибка добавления в БД: ", str(e))