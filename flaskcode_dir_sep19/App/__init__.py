from flask import Flask
from flask_session import Session

from App.models import db
from App.views import blue


def create_app():
    app = Flask(__name__)
    # init_extends(app)

    app.config['SECRET_KEY'] = '123456'
    app.config['SESSION_TYPE'] = 'redis'
    app.config['SESSION_KEY_PREFIX'] = 'python'
    se = Session()
    se.init_app(app=app)


    # dialect+driver://username:password@host:port/database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://qmx:123@localhost:3306/exercise'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app=app)

    return app
