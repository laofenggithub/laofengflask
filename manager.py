from flask.ext.script import Manager
from app import create_app, db
from flask_migrate import Migrate, MigrateCommand

app = create_app()
manager = Manager(app)

migrate = Migrate(app, db)
manager.add_command('db',MigrateCommand)

@manager.command
def dev():
    from livereload import Server
    live_server = Server(app.wsgi_app)
    live_server.watch('**/*.*')
    live_server.serve(open_url_delay=True)


@manager.command
def test():
    pass


@manager.command
def deploy():
    pass


if __name__ == '__main__':
    manager.run()
    # python manager.py shell 开启一个交互式执行程序
    # >>> from app import db
    # >>> from app import models
    # >>> db.create_all()
    # >>> from app.models import Role,User
    # >>> admins = Role(name='administrators')
    # >>> mod = Role(name='moderator')
    # >>> db.session.add_all([admins,mod])
    # >>> db.session.commit()
    # >>> ray = User(name='Ray',roles=admins)
    # >>> db.session.add(ray)
    # >>> db.session.commit()
    # >>> ray.password = '123456'
    # >>> db.session.add(ray) 更新
    # >>> db.session.commit()
    # >>> db.session.delete(ray)
    # >>> db.session.commit()
    # >>> User.query.all()
    # [<User 1>]
    # >>> Role.query.get(1)
    # <Role 1>
    # >>> User.query.get(1)
    # <User 1>
    # >>> print Role.query.get(2).name
    # moderator
    # >>> Role.query.filter(id>0).all()
    # [<Role 1>, <Role 2>]
    # >>> Role.query.filter(id>0)
    # <flask_sqlalchemy.BaseQuery object at 0x105d8ff50>
    # 执行函数：all() first() first_or_404() get() count() paginate()
    # 过滤函数：filter() filter_by() limit() offset() order_by() group_by()
