from flask import Blueprint

api = Blueprint('api', __name__)

@api.route('/', methods=["GET"])
def hello():
    print('request made')
    return "Welcome to ReceiptScanner."

