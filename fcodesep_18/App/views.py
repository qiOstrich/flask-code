from flask import Blueprint, render_template, url_for, request, session, make_response, Response, redirect, abort

blue = Blueprint('imblue', __name__)


@blue.route('/index/')
def index():
    return "index"


@blue.route('/main/')
def main():
    return '人间不值得'


@blue.route('/testreturn1/')
def testturn1():
    return render_template('testreturn1.html')


# 路由参数：
# 基本结构/资源路径/<变量>/
# 访问例：127.0.0.1/test/123/
# 路由参数和试图函数的参数名需要一致
# 路由参数可以规定类型，默认是字符串，格式：<type:name>
@blue.route('/test/<id>/')  # 不指定参数类型，默认字符串
def test(id):
    return '但你值得'


@blue.route('/test1/<string:id>/')
def test1(id):
    return id + '还给你'


@blue.route('/test2/<path:src>/')
def test2(src):
    return '这不都是你写的吗：' + src


@blue.route('/test3/<int:qian>/')
def test3(qian):
    return str(qian)


@blue.route('/test4/<any(a,b,c):list>/')
def test4(list):
    return 'test4'


@blue.route('/tologin/')
def toLogin():
    # username

    return render_template('login.html')


# methods元素不区分大小写
@blue.route('/login/', methods=['post', 'delete'])
def login():
    return '欢迎光临红浪漫，里面请'


# 状态码：
# 200 正确
# 301 重定向
# 302 永久重定向
# 403 防跨站攻击
# 404 路径错误
# 405 请求方式错误
# 500 服务器错误

@blue.route('/testpostman/')
def testpostman():
    uf = url_for('blue.testpostman')
    return '你的梦想是什么'


@blue.route('/testRequest/')
def testRequest():
    print(request.method)

    print(request.base_url)

    print(request.host_url)

    print(request.url)

    print(request.remote_addr)

    print(request.remote_user)

    print(request.files)

    print(request.headers)

    print(request.path)

    print(request.cookies)

    print(session)

    print(request.args.get('name'))

    print(request)

    return 'testRequest'


@blue.route('/testResponse/')
def testResponse():
    return 'string'


@blue.route('/testResponse2/')
def testResponse2():
    return render_template('testResponse2.html')


@blue.route('/testResponse3/')
def testResponse3():
    # 返回一个response类型
    return make_response('rap and roll')


@blue.route('/testResponse4/')
def testResponse4():
    resss = redirect(url_for('imblue.index'))
    return resss


@blue.route('/testResponse5/')
def testResponse5():
    s = Response('dsad')
    return s


# 异常
@blue.route('/testAbort/')
def testAbort():
    abort(405)
    return 'Abort'


@blue.errorhandler(405)
def testAbort1(Exeption):
    return '请停止访问'


# cookie的使用
# 需求：执行一个视图函数，longincookie.html
@blue.route('/tologincookie/')
def tologincookie():
    return render_template('logincookie.html')


@blue.route('/logincookie/', methods=['post'])
def logincookie():
    name = request.form.get('name')
    response = redirect(url_for('imblue.welcomecookie'))
    response.set_cookie('name', name)

    return response


@blue.route('//')
def logoutcookie():
    response = redirect(url_for('imblue.welcomecookie'))
    response.delete_cookie('name')
    return response


@blue.route('/welcomecookie/')
def welcomecookie():
    name = request.cookies.get('name', 'youke')

    return render_template('welcomecookie.html', name=name)
