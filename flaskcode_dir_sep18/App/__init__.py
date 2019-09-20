from flask import Flask
from flask_session import Session

from App.views import blue


def create_app():
    app = Flask(__name__)
    app.config['secret_key'] ='110'
    app.config['SESSION_TYPE']='redis'
    app.config['SESSION_KEY_PREFIX']='python1905'
    Session(app=app)
    app.register_blueprint(blueprint=blue)
    return app
