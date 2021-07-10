from database.db import db
from database.ma import ma
from flask_security import UserMixin, RoleMixin



class ItemModel(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    street = db.Column(db.String(50))

    def __init__(self, title, street):
        self.title = title
        self.street = street

    def __repr__(self):
        return '<Post %s>' % self.title

    @classmethod
    def find_by_name(cls, title):
        return cls.query.filter_by(title=title).first()

    @classmethod
    def find_all(cls):
        return cls.query.all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()



class ItemSchema(ma.Schema):
    class Meta:
        fields = ("id", "title", "street")





roles_users = db.Table('roles_users',
                       db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
                       db.Column('role_id', db.Integer(), db.ForeignKey('role.id')),
                       )

class User(db.Model, UserMixin):
    _tablename__ = 'User'
    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    roles = db.relationship('Role', secondary=roles_users, backref=db.backref('users', lazy='dynamic'))

class Role(db.Model, RoleMixin):
    _tablename__ = 'Role'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(255))
    description = db.Column(db.String(255))




