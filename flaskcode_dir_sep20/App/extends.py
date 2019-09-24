from flask_migrate import Migrate
from flask_session import Session

from App.models import db
from App.settings import Develop


def init_extends(app):
    app.config['secret_key'] = '12306'
    app.config['session_type'] = 'redis'
    Session(app=app)

    # app.config['sqlalchemy_database_uri'] = 'mysql+pymysql://qmx:123@localhost:3306/exercise'
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app=app)
    migrate = Migrate()
    migrate.init_app(app=app, db=db)
    
