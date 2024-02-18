# controllers/meeting_room_controller.py
from ..models import MeetingRoom

def get_all_meeting_rooms():
    return MeetingRoom.objects().all()
