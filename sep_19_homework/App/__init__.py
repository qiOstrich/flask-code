from flask import Flask

from App import settings
from App.extends import init_extendtion


def create_app(enviro):
    app = Flask(__name__)

    app.config.from_object(settings.ENVIRO.get(enviro.lower()))
    init_extendtion(app)

    return app
