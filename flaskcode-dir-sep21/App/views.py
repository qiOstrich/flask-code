from flask import Blueprint, render_template, request, url_for, current_app

from App.ext import cache
from App.models import Songs

blue = Blueprint('bp', __name__)


@blue.route('/')
def hello_world():
    return 'Hello World!'


@blue.route('/frombase/')
def frombase():
    # models class Songs
    # song_list = []
    # user_obj = User.query.filter(User.email.like('%' + email + '%')).paginate(int(page_index), int(page_size), False)
    page = int(request.args.get('page', 1))
    per_page = request.args.get('per_page', 5)
    paginate = Songs.query.paginate(page=page, per_page=per_page)
    # url = request.base_url
    # print(paginate.pages)
    # for song_query in paginate:
    #     song_list.append(song_query)
    return render_template('from_base.html', songs=paginate, base=url, page=str(page))


@blue.route('/HelloCache/')
@cache.cached(timeout=30)
def HelloCache():
    print('好的')
    return 'helloCache'


@blue.before_request
def beforeRequest():
    pass


@blue.route('/testTemConfig/')
def testTemConfig():
    return render_template('testTemConfig.html')


@blue.route('/testPythonConfig/')
def testPythonConfig():
    n = current_app.config
    print(type(n))
    print(n)
    return 'testPythonConfig'


@blue.route('/index/')
def index():
    # template 和 static的路径问题
    # 默认在当前文件夹中搜索template和static文件夹
    # 通过修改app=Flask(__name__,static_folder=绝对路径,template_folder=绝对路径)

    return 'index'


@blue.route('/testJosn/')
def testJosn():
    songs = Songs.query.all()
    song_list = []
    for song in songs:
        song_list.append(song.to_dict())
    data = {
        'msg': 'OK',
        'status': 200,
        'songs': song_list
    }
    return data


@blue.route('/getSongs/')
def getSongs():
    songs =Songs.query.paginate(1,2,False)
    return render_template('getSongs.html')


@blue.route('/oprator/', methods=['post', 'get', 'put', 'patch', 'delete'])
def oprator():
    if request.method == 'GET':
        return 'getted'
    elif request.method == 'POST':
        return 'posted'
    elif request.method == 'PUT':
        return 'putted'
    elif request.method == 'PATCH':
        return 'patched'
    elif request.method == 'DELETE':
        return 'deleted'
