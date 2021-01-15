from __init__.py import db

class User(db.Document):
    token = db.StringField()

class PanClient(db.Document):
    pan=db.StringField()
    name = db.StringField()
    dob=db.DateTimeField()
    father_name = db.StringField()
    client_id=db.StringField()
