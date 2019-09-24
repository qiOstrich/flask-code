from flask_bootstrap import Bootstrap
from flask_cache import Cache
from flask_migrate import Migrate
from flask_session import Session
import flask_debugtoolbar

from App.models import db

# cache = Cache(config={'CACHE_KEY_PREFIX': 'redis'})
cache = Cache(config={'CACHE_TYPE':'redis'})

def init_ext(app):
    app.config['secret_key'.upper()] = '120'
    app.config['session_type'.upper()] = 'redis'
    Session(app=app)

    db.init_app(app=app)

    migrate = Migrate()
    migrate.init_app(app=app, db=db)

    Bootstrap(app=app)

    app.debug = True
    dtb = flask_debugtoolbar.DebugToolbarExtension()
    dtb.init_app(app=app)

    # 如果报错 NO models name flask.extends
    cache.init_app(app=app)
