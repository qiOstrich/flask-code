from flask_migrate import MigrateCommand
from flask_script import Manager

from App import init_app

app = init_app('develop')

manager = Manager(app=app)
manager.add_command('db', MigrateCommand)
if __name__ == '__main__':
    manager.run()
