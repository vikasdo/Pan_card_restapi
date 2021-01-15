from flask import Flask
from flask_restx import Resource, Api
from pan import get_pan_data
app = Flask(__name__)
api = Api(app)
import time
import string 
import random 

from flask import Flask, jsonify, request
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)


# Setup the Flask-JWT-Extended extension
app.config['JWT_SECRET_KEY'] = 'secret_vikas_12AS'  # Change this!
jwt = JWTManager(app)

import re
 

def isValidPanCardNo(panCardNo):
 
    # Regex inorder for  check valid 
    # PAN Card number
    regex = "[A-Z]{5}[0-9]{4}[A-Z]{1}"
 
    p = re.compile(regex)
 
    # If the PAN Card number 
    # is empty return false
    if(panCardNo == None):
        return False
 
    # Return if the PAN Card number 
    # matched the ReGex 
    if(re.search(p, panCardNo) and
       len(panCardNo) == 10):
        return True
    else:
        return False




pan_card={}
# Provide a method to create access tokens. The create_access_token()
# function is used to actually generate the token, a
@app.route('/login', methods=['GET'])
def login():

   
    # Identity can be any data that is json serializable
    access_token = create_access_token(identity=time.time())
    return jsonify(access_token=access_token), 200


# Protect a view with jwt_required, which requires a valid access token
# in the request to access.
@app.route('/getclientid', methods=['POST'])
@jwt_required
def getclientid():
    # Access the identity of the current user with get_jwt_identity
    # current_user = get_jwt_identity()

    pannumber = request.json.get('pannumber', None)
    if not pannumber:
        return jsonify({"msg": "Missing pannumber parameter"}), 400

    if not  isValidPanCardNo(pannumber):
        return jsonify({"msg": "Not a Valid pannumber format "}), 401
    # print(pannumber)

  
    # initializing size of string  
    N = 7
      

    client_id = ''.join(random.choices(string.ascii_uppercase +
                                 string.digits, k = N)) 
    try:
        pan_card[client_id]=get_pan_data(pannumber)

    except:
        return jsonify({"msg": "Sorry Backend error Try again..."}), 400



    return jsonify(client_id=client_id), 200



@app.route('/getinfo', methods=['POST'])
@jwt_required
def getinfo():
    # Access the identity of the current user with get_jwt_identity
    try:
        current_user = get_jwt_identity()
        client_id = request.json.get('client_id', None)
        print(client_id,"---client_id")
        return jsonify(pannumber=pan_card[client_id]), 200
    except Exception as e:
        print(e)
        return jsonify({"msg": "client_id is not valid "}), 400



@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

if __name__ == '__main__':
    app.run(debug=True)

