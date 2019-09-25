from flask_cache import Cache
from flask_session import Session

from App.models import db

cache = Cache(config={'CACHE_TYPE': 'redis'})


def add_ext(app):
    app.config['secret_key'.upper()] = '12306'
    app.config['session_type'.upper()] = 'redis'
    Session(app=app)
    db.init_app(app=app)
    cache.init_app(app=app)
