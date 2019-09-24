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
    nickname = db.Column(db.String(20))
    true_name = db.Column(db.String(20))
    password = db.Column(db.String(40))
    age = db.Column(db.Integer)
    sex = db.Column(db.String(6))
    tel = db.Column(db.String(20))
    describe = db.Column(db.TEXT)
