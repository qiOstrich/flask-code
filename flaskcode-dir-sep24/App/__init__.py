import os

from flask import Flask

from App import settings
from App.ext import add_ext

static_folder = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'static')
template_folder = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'template')


def init_app(enviro):
    app = Flask(__name__, static_folder=static_folder, template_folder=template_folder)

    app.config.from_object(settings.ENV_SETTING.get(enviro))

    add_ext(app)

    return app
