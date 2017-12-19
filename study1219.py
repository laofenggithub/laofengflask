# coding=utf-8
from flask import Flask, url_for, request, render_template
from werkzeug.routing import BaseConverter
from flask.ext.script import Manager

class RegexConverter(BaseConverter):
    def __init__(self, url_map, *items):
        super(RegexConverter, self).__init__(url_map)
        self.regex = items[0]


app1 = Flask(__name__)
# 正则表达式路由
app1.url_map.converters['regex'] = RegexConverter
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


# 正则表达式路由
@app1.route('/user/<regex("[a-z]{3}"):userid>/')
def user(userid):
    return 'User %s' % userid

@app1.route('/login',methods=['GET', 'POST'])
def login():
    return render_template('login.html', method=request.method)


# test case
# with app.test_request_context('/login',method='POST'):
#     assert request.path == '/login'
#     assert request.method == 'POST'

if __name__ == '__main__':
    app1.run(host='0.0.0.0', debug=True)