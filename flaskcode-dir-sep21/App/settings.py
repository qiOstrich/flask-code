def get_database_uri(DATABASE):
    return '{dialect}+{driver}://{username}:{password}@{host}:{port}/{database}'.format(**DATABASE)


class Config():
    Test = False
    Debug = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopConfig(Config):
    Debug = True

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


class TestConfig(Config):
    Test = True

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


class ShowConfig(Config):
    Debug = True

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


class ProductConfig(Config):
    Debug = True

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


ENV_SETTING = {'develop': DevelopConfig,
               'test': TestConfig,
               'show': ShowConfig,
               'product': ProductConfig,
               }

if __name__ == '__main__':
    develop = DevelopConfig()
    print(develop.SQLALCHEMY_DATABASE_URI)
