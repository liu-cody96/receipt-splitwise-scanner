from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash # never store a plaintext password!!
from flask_jwt_extended import create_access_token,get_jwt,get_jwt_identity, \
                               unset_jwt_cookies, jwt_required, JWTManager

db = SQLAlchemy( )
cors = CORS( )
jwt = JWTManager( )

def create_app():
    """
    Implemented factory pattern for scalability and maintainability.
    Mainly it made it easier to set up and run tests. 
    """

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('config.settings')
    app.config.from_pyfile('settings.py', silent=True)

    db.init_app(app)
    cors.init_app(app)
    jwt.init_app(app)

    from .blueprints.routes import api
    app.register_blueprint(api)

    from .blueprints.users.auth import user
    app.register_blueprint(user)

    return app

