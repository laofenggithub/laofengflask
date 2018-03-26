from . import db, login_manager
from flask_login import UserMixin


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=True)
    users = db.relationship('User', backref='roles')

    @staticmethod
    def seed():
        db.session.add_all(map(lambda r: Role(name=r), ['Guests', 'Administrators']))
        db.session.commit()


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=True)
    password = db.Column(db.String, nullable=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    @staticmethod
    def on_created(self, target, value, initiator):
        target.roles = Role.query.filter_by(name='Guests').first()


# db.event.listen(User.name,'append',User.on_created)
db.event.listen(User.name, 'set', User.on_created)


@login_manager.user_loader
def get_user(user_id):
    # return User.query.filter_by(name=user_id).first()
    return User.query.get(int(user_id))