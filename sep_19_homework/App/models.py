from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class User(db.Model):
    # @staticmethod
    # def create_password(pwd):
    #     m = hashlib.md5()
    #     m.update(str(pwd).encode('utf-8'))
    #     passwd = m.hexdigest()
    #     return  passwd

    __tablename__ = 'user_info'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nickname = db.Column(db.String(20), nullable=False)
    true_name = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(40), nullable=False)
    age = db.Column(db.Integer, default=0)
    sex = db.Column(db.String(6), default='male')
    tel = db.Column(db.String(11))
    requ = db.Column(db.TEXT)
