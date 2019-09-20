from flask import Blueprint, render_template, make_response, request, redirect, url_for, session, abort

blue = Blueprint('blue', __name__)


@blue.route('/')
def main():
    rs = make_response('yes<a href="http://localhost:8888/tologincookie/">点击登录</a>')
    re = '来得正好'
    return re



@blue.route('/tologincookie/')
def tologincookie():
    ren = render_template('tologincookie.html')

    return ren


@blue.route('/logincookie/', methods=['post'])
def logincookie():
    username = request.form.get('username')
    session['username'] = username
    response = redirect(url_for('blue.welcomecookie'))

    return response


@blue.route('/welcomecookie/')
def welcomecookie():
    username = session.get('username')

    return render_template('welcomecookie.html', name=username)


@blue.route('/logoutcookie/')
def logoutcookie():
    try:
        session.pop('username')
    except:
        print('已经没得session了')
    response = redirect(url_for('blue.welcomecookie'))

    return response


#
# @blue.route('/tologincookie/')
# def tologincookie():
#     return render_template('tologincookie.html')
#
#
# @blue.route('/logincookie/', methods=['post'])
# def logincookie():
#     username = request.form.get('username')
#
#     response = redirect(url_for('blue.welcomecookie'))
#
#     response.set_cookie('username', username)
#     return response
#
#
# @blue.route('/logoutcookie/')
# def logourcookie():
#     response = redirect(url_for("blue.welcomecookie"))
#     response.delete_cookie("username")
#     return response
#
#
# @blue.route('/welcomecookie/')
# def welcomecookie():
#     username = request.cookies.get('username', '大爷')
#     return render_template('welcomecookie.html', name=username)

@blue.route('/teststring/<string:abc>/')
def teststring(abc):
    print(abc)
    return abc


@blue.route('/testint/<int:abc>/')
def testint(abc):
    print(abc)
    return str(abc)


@blue.route('/testfloat/<float:abc>/')
def testfloat(abc):
    return str(abc)


@blue.route('/testuuid/<uuid:abc>/')
def testuuid(abc):
    return str(abc)


@blue.route('/testpath/<path:abc>/')
def testpath(abc):
    return str(abc)


@blue.route('/testany/<any("1","2","3"):abc>/')
def testany(abc):
    return str(abc)


@blue.route('/testrequest/')
def testrequest():
    astr = 'path: '
    astr += request.path

    astr += '<br/>method: '
    astr += str(request.method)

    astr += '<br/>host: '
    astr += request.host

    astr += '<br/>host_url: '
    astr += request.host_url

    astr += '<br/>base_url: '
    astr += request.base_url

    astr += '<br/>url: '
    astr += request.url

    astr += '<br/>remote_addr: '
    astr += request.remote_addr

    astr += '<br/>args_getlist: '
    astr += str(request.args.getlist('name'))

    astr += '<br/>files: '
    astr += str(request.files)

    astr += '<br/>cookies: '
    astr += str(request.cookies.get('name'))

    astr += '<br/>headers: <br/>'
    astr += str(('<br/>').join(str(request.headers).split('\r\n')))

    # request.form.get()

    return astr


@blue.route('/testcookie/')
def testcookie():
    response = make_response('/testrequest/')
    response.set_cookie('name', 'how are you?')

    return response


@blue.route('/diy-except/')
def diy_except():
    abort(404)
    return '网页禁止访问'


@blue.errorhandler(404)
def handler_error(Exception):
    return '网站维护中'
