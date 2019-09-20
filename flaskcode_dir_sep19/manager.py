from flask_script import Manager

from App import create_app, blue

app = create_app()
app.register_blueprint(blueprint=blue)

manager = Manager(app=app)



if __name__ == '__main__':
    manager.run()
