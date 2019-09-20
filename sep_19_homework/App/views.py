from flask import Blueprint, render_template, request, session, redirect, url_for

from App.models import db, User

blue = Blueprint('bp', __name__)


@blue.route('/')
def main():
    db.create_all()
    return render_template('main.html')


@blue.route('/login/')
def login():
    try:
        session.pop('username')
    except:
        pass
    dictionary={}
    request.form.get('')

    return render_template('login.html')


@blue.route('/userinfo/', methods=['post'])
def userinfo():
    username = request.form.get('username')
    password = request.form.get('pwd')
    res = User.query.all()
    for i in res:
        if username == i.nickname and password == i.password:
            session['usename'] = username
            response = redirect(url_for('bp.userlist'))
            return response
    else:
        return '你输入的信息有误！<a href="http://localhost:8888/login/">点击重新登录</a>'


@blue.route('/register/')
def register():
    return 'OK'


@blue.route('/regist/')
def regist():
    return render_template('regist.html')


@blue.route('/userlist/')
def userlist():
    username = session.get('username')

    return render_template('userList.html')


@blue.route('/userdetail/')
def userdetail():
    session.get('username')

    return render_template('userDetail.html')
