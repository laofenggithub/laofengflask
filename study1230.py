# coding=utf-8
from flask import Flask
from os import path
from flask_sqlalchemy import SQLAlchemy
from flask.ext.script import Manager

basedir = path.abspath(path.dirname(__file__))

app = Flask(__name__)
manager = Manager(app)
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'sqlite:///' + path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(app)


@manager.command
def dev():
    from livereload import Server
    live_server = Server(app.wsgi_app)
    live_server.watch('**/*.*')
    live_server.serve(open_url_delay=True)


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=True)
    users = db.relationship('User', backref='roles')


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=True)
    password = db.Column(db.String, nullable=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))


if __name__ == '__main__':
    dev()
