from flask import Blueprint, render_template, request, session, redirect, url_for, make_response

from App import db
from App.models import Creature

blue = Blueprint('bl', __name__)


@blue.route('/')
def hello_world():
    return make_response('yes!<a href="/tologinsession/">登录</a>')


@blue.route('/tologinsession/')
def tologincookie():
    return render_template('tologinsession.html')


@blue.route('/loginsession/', methods=['post'])
def loginsession():
    name = request.form.get('username', 'badboy')

    session['username'] = name

    response = redirect(url_for('bl.welcome'))

    return response


@blue.route('/logoutsession/')
def logoutsession():
    response = redirect(url_for('bl.welcome'))

    try:
        session.pop('username')
    except:
        pass
    # response.delete_cookie('session')

    return response


@blue.route('/welcome/')
def welcome():
    name = session.get('username')
    return render_template('welcome.html', username=name)


@blue.route('/index/')
def index():
    return render_template('base_a.html')


# 宏定义
@blue.route('/testMacro/')
def testMacro():
    return render_template('base_b.html')


@blue.route('/testfor/')
def testfor():
    alist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    return render_template('base_c.html', alist=alist)


@blue.route('/testfilter/')
def testfilter():
    return render_template('base_d.html',
                           code='abcdefghijklmn',
                           code1='  fdhajkl   ',
                           code2='<a href="#">我可是一个a</a>',
                           )


@blue.route('/createTable/')
def createTable():
    db.create_all()
    return 'OK'


@blue.route('/dropTable/')
def dropTable():
    db.drop_all()
    return 'YEAP'


@blue.route('/alterTable/')
def alterTable():
    hen = Creature(name='小鸡崽子', color='colorful')

    db.session.add(hen)
    db.session.commit()
    return 'YES'


@blue.route('/queryall/')
def queryall():
    result = Creature.query.all()
    print(result)
    return str([result[0].name,result[0].color])
