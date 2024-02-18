# controllers/booking_controller.py
from ..models import Booking

def create_booking(room_id, date, start_time, end_time, booked_by):
    booking = Booking(room=room_id, date=date, start_time=start_time, end_time=end_time, booked_by=booked_by)
    booking.save()
    return booking
