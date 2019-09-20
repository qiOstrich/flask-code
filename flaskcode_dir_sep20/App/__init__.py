from flask import Flask

from App import settings
from App.extends import init_extends


def create_app(enviro):
    app = Flask(__name__)

    app.config.from_object(settings.ENV_SETTING.get(enviro.lower()))

    init_extends(app)

    return app
