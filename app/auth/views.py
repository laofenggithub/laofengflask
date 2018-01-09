# coding=utf-8
from flask import render_template, flash, redirect, url_for
from . import auth
from .forms import LoginForm, RegistrationForm
from .. import db
from ..models import User
from flask_login import login_user,logout_user

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    # flash(u'登录成功')
    if form.validate_on_submit():
        user = User.query.filter_by(name=form.username.data, password=form.password.data).first()
        if user is not None:
            login_user(user)
            return redirect(url_for('main.index'))

    return render_template('login.html',
                           title=u'登录',
                           form=form)


# @auth.route('/logout')
# def logout():
#     if current_user.is_authenticated():
#         logout_user()
#     return redirect('login')


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        user = User(email=form.email.data,
                    name=form.username.data,
                    password=form.password.data)

        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.login'))

    return render_template('register.html',
                           title=u'注册',
                           form=form)
