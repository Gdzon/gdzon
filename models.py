from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(session_options={"autoflush": False})


class Books(db.Model):
    id_ = db.Column(db.String, primary_key=True)
    subject = db.Column(db.String)
    description = db.Column(db.Text)
    grade = db.Column(db.Integer)
    author = db.Column(db.String)
    pub_h = db.Column(db.String)
    type = db.Column(db.String)
    tasks_count = db.Column(db.Integer)
    each_task_num = db.Column(db.Text)

    def __reps__(self):
        f"<Books {self.id}>"


def addBook(id_, subject, description, grade, author, pub_h, type, tasks_count):
    try:
        b = Books(id_=id_, subject=subject, description=description, grade=grade, author=author, pub_h=pub_h, type=type,
                  tasks_count=tasks_count)
        db.session.add(b)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print("Ошибка добавления в БД: ", str(e))
