# config.py

class Config:
    # Flask app configuration
    DEBUG = True

    # MongoDB configuration
    MONGODB_SETTINGS = {
        'db': 'meeting_room_booking',
        'host': 'mongodb://localhost:27017/meeting_room_booking'
    }
