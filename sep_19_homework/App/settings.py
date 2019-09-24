def get_database_uri(D):
    return '{dialect}+{driver}://{user}:{passwd}@{host}:{port}/{database}'.format(**D)


class Config():
    Test = False
    Debug = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopConfig(Config):
    Debug = True
    DATABASE = {
        'dialect': 'mysql',
        'driver': 'pymysql',
        'user': 'qmx',
        'passwd': '123',
        'host': 'localhost',
        'port': '3306',
        'database': 'exercise',
    }
    SQLALCHEMY_DATABASE_URI = get_database_uri(DATABASE)


class TestConfig(Config):
    Test = True
    DATABASE = {
        'dialect': 'mysql',
        'driver': 'pymysql',
        'user': 'qmx',
        'passwd': '123',
        'host': 'localhost',
        'port': '3306',
        'database': 'exercise',
    }
    SQLALCHEMY_DATABASE_URI = get_database_uri(DATABASE)


class ShowConfig(Config):
    Debug = True
    DATABASE = {
        'dialect': 'mysql',
        'driver': 'pymysql',
        'user': 'qmx',
        'passwd': '123',
        'host': 'localhost',
        'port': '3306',
        'database': 'exercise',
    }
    SQLALCHEMY_DATABASE_URI = get_database_uri(DATABASE)


class ProductConfig(Config):
    Debug = True
    DATABASE = {
        'dialect': 'mysql',
        'driver': 'pymysql',
        'user': 'qmx',
        'passwd': '123',
        'host': 'localhost',
        'port': '3306',
        'database': 'exercise',
    }
    SQLALCHEMY_DATABASE_URI = get_database_uri(DATABASE)


ENVIRO = {
    'develop':DevelopConfig,
    'test':TestConfig,
    'show':ShowConfig,
    'product':ProductConfig,
}