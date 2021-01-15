from flask_mongoengine import MongoEngine

from main import app
app.config['MONGODB_SETTINGS'] = {
    'db': 'user',
    'host': 'mongodb+srv://vikas:123@cluster0.bj4nr.mongodb.net/user?retryWrites=true&w=majority',
  
}
db = MongoEngine()
db.init_app(app)