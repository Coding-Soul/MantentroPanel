from flask import Blueprint, request
from src.user.database import create_user as create_user, list_users, delete_user

users_bp = Blueprint('users', __name__)


# Create user route
@users_bp.route('/api/user/create', methods=['POST'])
def user_create():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        rs = create_user(username=username, email=email, password=password)
        return rs


# User list
@users_bp.route('/api/user/list', methods=['GET'])
def user_list():
    output = list_users()
    return output


# User delete
@users_bp.route('/api/user/delete', methods=['POST'])
def user_delete():
    if request.method == 'POST':
        user_id = request.form['id']
        rs = delete_user(user_id)  # Getting result & delete the user
        return rs  # returning
