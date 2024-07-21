from flask import Blueprint, request
from src.user.database import create_user as create_user
from src.user.database import list_users

users_bp = Blueprint('users', __name__)


# Create user route
@users_bp.route('/api/user/create', methods=['POST'])
def user_create():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        create_user(username=username, email=email, password=password)
        return 'idk'


# User list
@users_bp.route('/api/user/list')
def user_list():
    output = list_users()
    return f"User-List: {output}"
