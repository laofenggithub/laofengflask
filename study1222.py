# coding=utf-8
from flask import Flask, render_template, request, make_response
from livereload import Server

from os import path
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import *

app = Flask(__name__)
Bootstrap(app)
nav = Nav()

nav.register_element('top',Navbar(u'Flask入门',
                                  View(u'主页','index'),
                                  View(u'关于','about'),
                                  View(u'服务','services')
                                  ))

nav.init_app(app)



@app.route('/')
def index():
    return render_template('index1222.html',title='Welcome')

@app.route('/services')
def services():
    return 'Service'

@app.route('/about')
def about():
    return 'About'

if __name__ == '__main__':
    live_server = Server(app.wsgi_app)
    live_server.watch('**/*.*')
    live_server.serve(open_url_delay=True)
