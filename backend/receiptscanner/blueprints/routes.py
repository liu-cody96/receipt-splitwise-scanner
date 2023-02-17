from flask import Blueprint
from flask import request, jsonify
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash # never store a plaintext password!!
from flask_jwt_extended import create_access_token,get_jwt_identity, \
                               unset_jwt_cookies, jwt_required

api = Blueprint('api', __name__)
CORS(api)

@api.route('/', methods=["GET"])
def hello():
    print('request made')
    return "Welcome to ReceiptScanner."

@api.route('/receiptscanner', methods=["POST"])
@jwt_required() # protect this route with JWT required. only if you pass in a token you can view this route
def display_button():

    if request.method == 'POST':
        import requests
        receiptOcrEndpoint = 'https://ocr.asprise.com/api/v1/receipt'
        imageFile = request.files['image'].read()
    """
    r = requests.post(receiptOcrEndpoint, data = { \
        'api_key': 'TEST',        # Use 'TEST' for testing purpose \
        'recognizer': 'US',       # can be 'US', 'CA', 'JP', 'SG' or 'auto' \
        'ref_no': 'ocr_python_123', # optional caller provided ref code \
    }, \
    files = {"file": imageFile})

    receipt_json = r.json() # result in JSON
    res = {
        'merchant_name': receipt_json['receipts'][0]['merchant_name'],
        'items': receipt_json['receipts'][0]['items'],
        'tax': receipt_json['receipts'][0]['tax'],
        'service_charge': receipt_json['receipts'][0]['service_charge'],
        'tip': receipt_json['receipts'][0]['tip'],
        'total': receipt_json['receipts'][0]['total']
    }
    """
    import random 
    res = {
        'merchant_name': "<Unable to be parsed>" + str(random.randint(1,10))
    }

    return jsonify(res), 200


