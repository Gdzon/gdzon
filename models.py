from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    grade = db.Column(db.Integer, unique=True, nullable=False)
    cover = db.Column(db.String)
    tasks = db.Column(db.String)
    author = db.Column(db.String)

    def __reps__(self):
        f"<Books {self.id}>"