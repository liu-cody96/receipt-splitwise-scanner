from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash # never store a plaintext password!!

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config.settings')
app.config.from_pyfile('settings.py', silent=True)
CORS(app)
db = SQLAlchemy(app)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True) # unique means no user can have the same email
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))


@app.route('/')
def index():
    """
    Render a Hello World response.

    :return: Flask response
    """

    return "HELLO WORLD"

@app.route('/register', methods=['GET', 'POST'])
def register():
    """
    Add a user to the database.
    """
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = Users.query.filter_by(email=email).first()
        if user:
            return 'Email already in use.'
        elif len(email) < 4:
            return 'Email must be > 3 chars long'
        elif len(first_name) < 2:
            return 'First name must be > 1 character'
        elif password1 != password2:
            return 'Passwords don\'t match'
        elif len(password1) < 7:
            return 'Password must be longer than 7 chars'
        else:
            # add user to database
            new_user = Users(email=email, first_name = first_name, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user) # add new user
            db.session.commit() # commit changes to DB and update DB

            return first_name
    