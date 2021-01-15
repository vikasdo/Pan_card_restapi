
from mongoengine import connect
# connect("mongodb+srv://vikas:123@cluster0.bj4nr.mongodb.net/user?retryWrites=true&w=majority")

# connect( db='user', username='vikas', password='123', host='mmongodb+srv://vikas:123@cluster0.bj4nr.mongodb.net/user')
from datetime import datetime


from flask import Flask
from flask_mongoengine import MongoEngine

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'db': 'user',
    'host': 'mongodb+srv://vikas:123@cluster0.bj4nr.mongodb.net/user?retryWrites=true&w=majority',
  
}
db = MongoEngine()
db.init_app(app)
class User(db.Document):
    token = db.StringField()

class PanClient(db.Document):
    pan=db.StringField()
    name = db.StringField()
    dob=db.DateTimeField()
    father_name = db.StringField()
    client_id=db.StringField()
pan_card={
    "pan": "ANRPM2537J",
    "name": "Dinesh Kumar",
    "dob": "1990-10-25",
    "father_name": "Hari Kumar",
    "client_id": "4feb601e-2316-4dda-8d91-28c89cdb2335"
}
from datetime import datetime
s = pan_card['dob']
print(s)
# User(user='laura', token='lAJh12').save()
PanClient(pan=pan_card['pan'],name=pan_card['name'],dob=s,father_name=pan_card['father_name'],client_id='ASA123A1').save()

print(PanClient.objects.first().to_json())
if __name__ == "__main__":
    app.run(debug=True)