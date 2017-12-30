# coding=utf-8
from flask import url_for, request, render_template,redirect,make_response,abort,flash

def init_views(app):
    @app.route('/login', methods=['GET', 'POST'])
    def login():
        from forms import LoginForm
        form = LoginForm()
        flash(u'登录成功')
        return render_template('login.html', title=u'登录', form=form)

    @app.route('/')
    def index():
        return render_template('index.html',title='Welcome')

    @app.route('/services')
    def services():
        return 'Service'

    @app.route('/about')
    def about():
        return 'About'
