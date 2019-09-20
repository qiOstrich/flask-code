from flask import Flask

from App.models import db
from App.views import blue


def create_app():
    app = Flask(__name__)
    app.register_blueprint(blueprint=blue)
    app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://qmx:123@localhost:3306/exercise'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
    app.config['session_key'] = '12306'
    db.init_app(app=app)
    return app
