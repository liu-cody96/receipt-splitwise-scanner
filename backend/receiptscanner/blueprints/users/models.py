from ...app import db

class Users(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True) # unique means no user can have the same email
    password = db.Column(db.String(150))
    username = db.Column(db.String(150))