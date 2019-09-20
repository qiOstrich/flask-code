from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    __tablename__='You'
    id = db.Column(db.Integer,primary_key=True)
    name= db.Column(db.String(20))
    age = db.Column(db.Integer)

