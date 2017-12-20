# coding=utf-8
from flask import Flask, url_for, request, render_template,redirect,make_response,abort
from werkzeug.routing import BaseConverter
from werkzeug.utils import secure_filename

from os import path
# from flask.ext.script import Manager

# 正则表达式路由
'''
class RegexConverter(BaseConverter):
    def __init__(self, url_map, *items):
        super(RegexConverter, self).__init__(url_map)
        self.regex = items[0]
'''
app1 = Flask(__name__)
# 正则表达式路由
# app1.url_map.converters['regex'] = RegexConverter
# flask路由
'''
@app.route('/')
def hello_world():
    return 'Hello World!'

# @app.route('/<any(a,b):page_name>/') *understand
@app.route('/user/<uname>')
def hello_world1(uname):
    return 'Hello World! %s' % uname

# test case
# with app.test_request_context():
#     print url_for('hello_world1',uname='jimu')
# test case
# with app.test_request_context('/login',method='POST'):
#     assert request.path == '/login'
#     assert request.method == 'POST'

# static/style.css
# url_for('static', filename='style.css')

@app.route('/login',methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        hello_world()
    else:
        hello_world1('loginname')

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)
'''
# 正则表达式路由,get,post响应
'''
@app1.route('/user/<regex("[a-z]{3}"):userid>/')
def user(userid):
    return 'User %s' % userid

@app1.route('/login',methods=['GET', 'POST'])
def login():
    return render_template('login.html', method=request.method)
'''
# 文件上传
'''
@app1.route('/upload',methods=['GET','POST'])
def upload():
    if request.method=='POST':
        f = request.files['file']
        basepath = path.abspath(path.dirname(__file__))
        upload_path=path.join(basepath,'static/uploads')
        f.save(upload_path,secure_filename(f.filename))
        return redirect(url_for('upload'))
    return render_template('upload.html')
'''
# cookic获取
#     request.cookies['aa']
@app1.route('/')
def index():
    # abort(400)
    response = make_response(render_template('index.html',title='Welcome'))
    response.set_cookie('username','')
    return response

@app1.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app1.run(host='0.0.0.0', debug=True)