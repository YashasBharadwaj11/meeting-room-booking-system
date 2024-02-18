from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required, current_user
from .models import MeetingRoom, Booking
from app.models import User
bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/meeting_rooms', methods=['GET'])
def get_meeting_rooms():
    rooms = MeetingRoom.objects().to_json()
    return rooms

@bp.route('/bookings', methods=['POST'])
@login_required
def create_booking():
    data = request.json
    room_id = data.get('room_id')
    date = data.get('date')
    start_time = data.get('start_time')
    end_time = data.get('end_time')

    # Check if room is available for the given date and time
    if Booking.objects(room=room_id, date=date, start_time__lte=end_time, end_time__gte=start_time).first():
        return jsonify({'error': 'Room already booked for the selected time slot'}), 400

    # Create booking
    booking = Booking(room=room_id, date=date, start_time=start_time, end_time=end_time, booked_by=current_user)
    booking.save()
    return jsonify({'message': 'Booking created successfully'}), 201

@bp.route('/register', methods=['POST'])
def register_user():
    # Get data from request
    data = request.json

    # Extract user data from request
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    # Check if username or email already exists
    existing_user = User.objects(username=username) or User.objects(email=email)
    if existing_user:
        return jsonify({'error': 'User already exists'}), 400
    
    # Create a new user
        new_user = User(username=username, email=email, password=password)
        new_user.save()

        return jsonify({'message': 'User registered successfully'}), 201
    
@bp.route('/login', methods=['POST'])
def login_user():
    # Get data from request
    data = request.json

    # Extract login credentials from request
    username = data.get('username')
    password = data.get('password')

    # Find user by username
    user = User.objects(username=username).first()

    # Check if user exists and password matches
    if user and user.check_password(password):
        # Return success response
        return jsonify({'message': 'Login successful', 'user_id': str(user.id)}), 200
    else:
        # Return error response
        return jsonify({'error': 'Invalid username or password'}), 401

