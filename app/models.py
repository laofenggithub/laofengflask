from . import db


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=True)
    users = db.relationship('User', backref='roles')

    @staticmethod
    def seed():
        db.session.add_all(map(lambda r: Role(r), ['Guests', 'Administrators']))
        db.session.commit()


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=True)
    password = db.Column(db.String, nullable=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    @staticmethod
    def on_created(target, value, initiator):
        target.roles = Role.query.filter_by(name='Guests').first()

db.event.listen(User.name,'append',User.on_created)