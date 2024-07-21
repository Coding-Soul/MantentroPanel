from flask import Blueprint

home_bp = Blueprint('home', __name__)


# Home route
@home_bp.route('/')
def home():
    return 'API is running on flask...'
