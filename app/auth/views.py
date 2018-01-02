from flask import render_template, flash
from . import auth


@auth.route('/login', methods=['GET', 'POST'])
def login():
    from app.auth.forms import LoginForm
    form = LoginForm()
    flash(u'登录成功')
    return render_template('login.html', title=u'登录', form=form)


# @auth.route('/logout')
# def logout():
#     if current_user.is_authenticated():
#         logout_user()
#     return redirect('login')


@auth.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('register.html', title=u'注册')
