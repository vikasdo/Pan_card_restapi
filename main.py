from flask import Flask
from flask_restx import Resource, Api
from pan import get_pan_data
app = Flask(__name__)
api = Api(app)
import time
import string 
import random 
# from models import User,PanClient
from flask import Flask, jsonify, request
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)
from flask_mongoengine import MongoEngine
import re
app.config['MONGODB_SETTINGS'] = {
    'db': 'user',
    'host': 'mongodb+srv://vikas:123@cluster0.bj4nr.mongodb.net/user?retryWrites=true&w=majority',
  
}
db = MongoEngine()
db.init_app(app)

# MODELS 
class User(db.Document):
    token = db.StringField()

class PanClient(db.Document):
    pan=db.StringField()
    name = db.StringField()
    dob=db.DateTimeField()
    father_name = db.StringField()
    client_id=db.StringField()


# Setup the Flask-JWT-Extended extension
app.config['JWT_SECRET_KEY'] = 'secret_vikas_12AS'  # Change this!
jwt = JWTManager(app)


 

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
@api.route('/login')
class login(Resource):

   
   def get(self):
        # Identity can be any data that is json serializable
        access_token = create_access_token(identity=time.time())
        User( token=access_token).save()

        return (access_token)




@api.route('/getclientid')
class Getclientid(Resource):
    @api.doc(
        "Get a specific user",
        responses={
            200: ("User data successfully sent"),
            404: "User not found!",
        },
    )
    # Access the identity of the current user with get_jwt_identity
    # current_user = get_jwt_identity()
    @jwt_required
    def post(self):
        pannumber = request.json.get('pannumber', None)
        if not pannumber:
            return {"msg": "Missing pannumber parameter"},400

        if not  isValidPanCardNo(pannumber):
            return {"msg": "Not a Valid pannumber format "},400

      
        # initializing size of string  
        N = 7
          

        client_id_s= ''.join(random.choices(string.ascii_uppercase +
                                     string.digits, k = N)) 
        try:
            pan_card=get_pan_data(pannumber)
            PanClient(pan=pan_card['pan'],name=pan_card['name'],dob=str(pan_card['dob']),father_name=pan_card['father_name'],client_id=client_id_s).save()
            print(pan_card)
        except Exception as e:
            print(e)

            return ({"msg": "Sorry Backend error Try again..."}), 400



        return (client_id_s), 200


@api.route('/getinfo')
class getinfo(Resource):
    # Access the identity of the current user with get_jwt_identity
    @jwt_required
    def post(self):
        try:
            current_user = get_jwt_identity()
            client_id = request.json.get('client_id', None)
            print(client_id,"---client_id")
            return PanClient.objects(client_id=client_id).first().to_json(), 200
        except Exception as e:
            print(e)
            return ({"msg": "client_id is not valid "}), 400




if __name__ == '__main__':
    app.run(debug=True)

