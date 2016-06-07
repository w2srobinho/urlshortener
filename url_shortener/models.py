from . import db

class User(db.Model):
    """
    Database model from User with id and name properties
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    urls = db.relationship('Url', backref='owner', lazy='dynamic')


class Url(db.Model):
    """
    Database model from Url with id, hits and owner properties
    """
    id = db.Column(db.Integer, primary_key=True)
    hits = db.Column(db.Integer)
    address = db.Column(db.String(200))
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))
