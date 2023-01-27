from extensions import db # from the current website folder import db 
from flask_login import UserMixin
from sqlalchemy.sql import func # 

"""
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now()) # func.now gets the current date and teim and we store that as the current value
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) # must pass a valid id of existing user here
    # this is a one to many relationship. one user has many notes 
"""


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True) # unique means no user can have the same email
    password = db.Column(db.String(150))
    username = db.Column(db.String(150))
    # notes = db.relationship('Note') # will allow us to access all notes within Note table for a given user. 
    