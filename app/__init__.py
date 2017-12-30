# coding=utf-8
from flask import Flask
from werkzeug.routing import BaseConverter
from os import path
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_sqlalchemy import SQLAlchemy
from flask_nav.elements import *
from .views import init_views

# 正则表达式路由
class RegexConverter(BaseConverter):
    def __init__(self, url_map, *items):
        super(RegexConverter, self).__init__(url_map)
        self.regex = items[0]


basedir = path.abspath(path.dirname(__file__))

bootstrap = Bootstrap()
nav = Nav()
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.url_map.converters['regex'] = RegexConverter
    app.config.from_pyfile('config')
    app.config['SQLALCHEMY_DATABASE_URI'] = \
        'sqlite:///' + path.join(basedir, 'data.sqlite')
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
    nav.register_element('top', Navbar(u'Flask入门',
                                       View(u'主页', 'index'),
                                       View(u'关于', 'about'),
                                       View(u'服务', 'services')
                                       ))
    db.init_app(app)
    bootstrap.init_app(app)
    nav.init_app(app)
    init_views(app)
    # 类似于插件的模式，将应用插入到各个功能里
    return app