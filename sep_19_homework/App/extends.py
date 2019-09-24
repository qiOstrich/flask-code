from flask_migrate import Migrate
from flask_session import Session

from App.models import db


def init_extendtion(app):
    db.init_app(app=app)

    session_key = 'secret_key'
    session_type = 'session_type'
    app.config[session_key.upper()] = '12306'
    app.config[session_type.upper()] = 'redis'
    Session(app=app)

    migrate =Migrate()
    migrate.init_app(app=app,db=db)