from flask import Blueprint, render_template, request, session, redirect, url_for, make_response

from App.models import db, User

blue = Blueprint('bp', __name__)


@blue.route('/')
def main():
    return render_template('main.html')


@blue.route('/login/')
def login():
    username = session.get('username', 'root')
    pwd = session.get('pwd')
    return render_template('login.html', username=username, pwd=pwd)


@blue.route('/logout/')
def logout():
    print('yes')
    response = redirect(url_for('bp.login'))
    try:
        session.pop('pwd')
    except:
        pass
    session['pwd'] = 'You do not have a password.'

    return response


@blue.route('/userinfo/', methods=['post', 'get'])
def userinfo():
    name = request.form.get('username', 'have not user')
    password = request.form.get('pwd')
    res = User.query.filter(User.nickname == name)
    if res.count() > 0:
        if password == res[0].password:
            session['usename'] = name
            response = redirect(url_for('bp.userdetail'))
            return response
        else:
            return '你输入的密码错误！<a href="' + request.host_url + 'login/">点击重新登录</a>'
    else:
        return '你输入的账号不存在！<a href="' + request.host_url + 'login/">点击重新登录</a>'


@blue.route('/regist/')
def regist():
    return render_template('regist.html')


@blue.route('/userdetail/', methods=['post', 'get'])
def userdetail():
    user = session.get('usename')
    print(user)
    res = User.query.filter(User.nickname == user)[0]
    photo = request.files.get('file1', 'none')

    return render_template('userDetail.html', name=res.nickname, tel=res.tel, describe=res.describe, photo=photo)


@blue.route('/userlist/')
def userlist():
    page = int(request.args.get('page', 1))
    per_page = request.args.get('per_page', 5)
    users = User.query.paginate(page=page, per_page=per_page)
    return render_template('userList.html', users=users, page=str(page))


@blue.route('/deleteUser/')
def deleteUser():
    username = request.args.get('deletename')
    name = User.query.filter(User.nickname == username)[0]
    db.session.delete(name)
    db.session.commit()
    response = redirect(url_for(('bp.userlist')))
    return response


@blue.route('/updateUser/')
def updateUser():
    nickname = request.args.get('nickname')
    use_nickname = User.query.filter(User.nickname == nickname)[0]

    return render_template('update.html', user=use_nickname)


@blue.route('/update/',methods=['post','get'])
def update():
    nickname = request.form.get('username')
    true_name = request.form.get('name')
    age = request.form.get('age')
    sex = request.form.get('sex')
    tel = request.form.get('phone')
    describe = request.form.get('ask')
    current_user = User.query.filter(User.nickname == nickname)[0]
    current_user.nickname = nickname
    current_user.true_name = true_name
    current_user.age = int(age)
    current_user.sex = sex
    current_user.tel = tel
    current_user.descrbi = describe
    db.session.add(current_user)
    db.session.commit()
    session.pop('usename')
    session['usename'] = nickname

    return '修改成功'


@blue.route('/addUser/', methods=['post'])
def addUser():
    try:
        username = request.form.get('username')
        true_name = request.form.get('name')
        passwd = request.form.get('pwd')
        age = request.form.get('age')
        sex = request.form.get('sex')
        tel = request.form.get('phone')
        describe = request.form.get('ask')
        # checknum = request.form.get('number')
    except:
        return '填写信息错误'
    old_name = User.query.filter(User.nickname == username)
    try:
        print(old_name[0].nickname)
    except:
        pass

    if old_name.count() > 0 and username == 'none':
        return make_response("<a href=" + request.host_url + "regist>用户名不可为空，且不可重复。请重新填写</a>")
    elif not true_name:
        return make_response("<a href=" + request.host_url + "regist>真实姓名不可为空，请重新填写</a>")
    elif not passwd:
        return make_response("<a href=" + request.host_url + "regist>密码不可为空，请重新填写</a>")
    elif not age:
        return make_response("<a href=" + request.host_url + "regist>年龄不可为空，请重新填写</a>")

    new_user = User()
    new_user.nickname = username
    new_user.true_name = true_name
    new_user.password = passwd
    new_user.age = int(age)
    new_user.sex = sex
    new_user.tel = tel
    new_user.describe = describe

    db.session.add(new_user)
    db.session.commit()

    session['username'] = request.form.get('username')
    session['pwd'] = request.form.get('pwd')

    return render_template('login.html', username=username, pwd=passwd)
