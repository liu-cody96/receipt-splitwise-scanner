from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash # never store a plaintext password!!
from flask_jwt_extended import create_access_token,get_jwt,get_jwt_identity, \
                               unset_jwt_cookies, jwt_required, JWTManager

main_app = Flask(__name__, instance_relative_config=True)
main_app.config.from_object('config.settings')
main_app.config.from_pyfile('settings.py', silent=True)
CORS(main_app)
db = SQLAlchemy(main_app)
jwt = JWTManager(main_app)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True) # unique means no user can have the same email
    password = db.Column(db.String(150))
    username = db.Column(db.String(150))

@main_app.route('/', methods=["GET"])
def hello():
    print('request made')
    return "Hello world"

@main_app.route('/token', methods=["POST"])
def create_token():
    email = request.json.get("email", None)
    password = request.json.get("password", None)
    user = Users.query.filter_by(email=email).first()
    if not user or not(check_password_hash(user.password, password)):
        return {"msg": "Wrong email or password"}, 401

    # if login is correct, create an access token and return the response to the frontend
    access_token = create_access_token(identity=email)
    response = {"access_token":access_token}
    return response


@main_app.route('/profile')
@jwt_required() # protect this route with JWT required. only if you pass in a token you can view this route
def my_profile():
    current_user = get_jwt_identity()

    # fetch all details of the current user from the DB. 
    user = Users.query.filter_by(email=current_user).first()

    response = jsonify({"username": user.username})
    return response, 200

@main_app.route("/logout", methods=["POST"])
def logout():
    response = jsonify({"msg": "logout successful"})
    unset_jwt_cookies(response)
    return response

@main_app.route('/register', methods=['GET', 'POST'])
def register():
    """
    Add a user to the database.
    """
    if request.method == 'POST':
        email = request.json['email']
        username = request.json['userName']
        password1 = request.json['password1']
        password2 = request.json['password2']
        

        user = Users.query.filter_by(email=email).first()
        if user:
            return {'errorMsg': 'Email already in use.'}, 400
        elif len(email) < 4:
            return {'errorMsg': 'Email must be > 3 chars long'}, 400
        elif len(username) < 2:
            return {'errorMsg': 'Username must be > 1 character'}, 400
        elif password1 != password2:
            return {'errorMsg': 'Passwords don\'t match'}, 400
        elif len(password1) < 7:
            return {'errorMsg':'Password must be longer than 7 chars'}, 400
        else:
            # add user to database
            new_user = Users(email=email, username=username, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user) # add new user
            db.session.commit() # commit changes to DB and update DB

            return username + "Created!"
    