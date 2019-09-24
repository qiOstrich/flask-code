def get_database_uri(DATABASE):
    return '{dialect}+{driver}://{username}:{password}@{host}:{port}/{database}'.format(**DATABASE)


class Config():
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class Develop(Config):
    DATABASE = {
        'dialect': 'mysql',
        'driver': 'pymysql',
        'username': 'qmx',
        'password': '123',
        'host': 'localhost',
        'port': '3306',
        'database': 'study',
    }
    SQLALCHEMY_DATABASE_URI = get_database_uri(DATABASE)


class Test(Config):
    DATABASE = {
        'dialect': 'mysql',
        'driver': 'pymysql',
        'username': 'qmx',
        'password': '123',
        'host': 'localhost',
        'port': '3306',
        'database': 'study',
    }
    SQLALCHEMY_DATABASE_URI = get_database_uri(DATABASE)


class Show(Config):
    DATABASE = {
        'dialect': 'mysql',
        'driver': 'pymysql',
        'username': 'qmx',
        'password': '123',
        'host': 'localhost',
        'port': '3306',
        'database': 'study',
    }
    SQLALCHEMY_DATABASE_URI = get_database_uri(DATABASE)


class Product(Config):
    DATABASE = {
        'dialect': 'mysql',
        'driver': 'pymysql',
        'username': 'qmx',
        'password': '123',
        'host': 'localhost',
        'port': '3306',
        'database': 'study',
    }
    SQLALCHEMY_DATABASE_URI = get_database_uri(DATABASE)
ENV_SETTING={'develop':Develop,
             'test':Test,
             'show':Show,
             'product':Product,
             }

if __name__ == '__main__':
    develop = Develop()
    print(develop.SQLALCHEMY_DATABASE_URI)
