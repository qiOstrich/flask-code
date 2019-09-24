from flask import Flask

from App import settings
from App.ext import init_ext


def create_app(env):
    app = Flask(__name__)

    app.config.from_object(settings.ENV_SETTING.get(env.lower()))

    init_ext(app)

    return app
