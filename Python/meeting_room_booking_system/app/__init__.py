# from flask import Flask
# from flask_mongoengine import MongoEngine
# from flask_login import LoginManager
# from .routes import bp
# # Initialize Flask app
# app = Flask(__name__)

# # Load configurations from config.py
# app.config.from_pyfile('../config.py')

# # Initialize MongoEngine
# db = MongoEngine(app)

# # Initialize Flask-Login
# login_manager = LoginManager()
# login_manager.init_app(app)

# # Import routes
# from app import routes

# app.register_blueprint(bp)

# # Import models (ensure they are imported after initializing db)
# from app.models import User

# @login_manager.user_loader
# def load_user(user_id):
#     return User.objects(id=user_id).first()


from flask import Flask
from flask_mongoengine import MongoEngine
from flask_login import LoginManager
from flask_cors import CORS

# Initialize MongoEngine
db = MongoEngine()

# Initialize Flask-Login
login_manager = LoginManager()

def create_app():
    # Initialize Flask app
    app = Flask(__name__)

    # Load configurations from config.py
    app.config.from_pyfile('../config.py')

    # Initialize MongoEngine with the Flask app
    db.init_app(app)

    # Initialize Flask-Login with the Flask app
    login_manager.init_app(app)

    # Import and register blueprints
    from .routes import bp
    app.register_blueprint(bp)

    # Import models (ensure they are imported after initializing db)
    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.objects(id=user_id).first()

    CORS(app)

    return app
