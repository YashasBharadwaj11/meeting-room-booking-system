from flask_mongoengine import MongoEngine
from flask_login import UserMixin

db = MongoEngine()

class User(UserMixin, db.Document):
    username = db.StringField(unique=True)
    email = db.EmailField(unique=True)
    password = db.StringField()
    role = db.StringField(default='user')  # Can be 'user' or 'admin'

class MeetingRoom(db.Document):
    room_id = db.StringField(unique=True)
    capacity = db.IntField()

class Booking(db.Document):
    room = db.ReferenceField(MeetingRoom)
    date = db.DateTimeField()
    start_time = db.DateTimeField()
    end_time = db.DateTimeField()
    booked_by = db.ReferenceField(User)
