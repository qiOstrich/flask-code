from flask import Blueprint, request

from App.models import db, User

blue = Blueprint('bp', __name__)


@blue.route('/main/<string:abs>/')
def hello_world(abs):
    name = request.args.get('name')
    metho = [request.method,
             request.base_url,
             request.host_url,
             request.url,
             request.remote_addr,
             request.remote_user,
             request.files,

             request.path,
             # request.headers,

             ]
    print(metho, name)
    return 'Hello World!'


@blue.route('/createTable/')
def createTable():
    db.create_all()
    return '创建表成功'


@blue.route('/dropTable/')
def dropTable():
    db.drop_all()
    return '删除表成功'


@blue.route('/addUser/')
def addUser():
    asd = User()
    asd.name = 'Tom'
    asd.age = 18
    db.session.add(asd)
    db.session.commit()

    return 'OK'


@blue.route('/addUserList/')
def addUserList():
    j = User(name='Hellen', age=20)
    l = User(name='Lucky', age=19)
    liat_s = [j, l]

    ds = db.session
    ds.add_all(liat_s)
    ds.commit()

    return 'YES!!'


@blue.route('/updateUser/')
def updateUser():
    u = User.query.first()
    u.name = 'Jerry'
    u.age = 22
    db.session.add(u)
    db.session.commit()
    return 'update OK'

@blue.route('/queryUser/')
def queryUser():
    res = User.query.order_by(db.desc('age'))
    for i in res :
        print(i.name,i.age)
    return 'Done'