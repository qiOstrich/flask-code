from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Creature(db.Model):

    __tablename__='Animals'
    id =db.Column(db.Integer,primary_key=True,autoincrement=True)

    name = db.Column(db.String(22))

    color = db.Column(db.String(15))

