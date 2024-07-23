from flask import Blueprint, request, session, redirect, url_for
from src.ServerManager import servers
from markupsafe import escape
import os
from src.user.database import hash_password, verify_password, list_users

login_bp = Blueprint('login', __name__)


# Route for login
@login_bp.route('/login', methods=['POST', 'GET'])
def user_login():
    if request.method == 'POST':

        name = request.form['name']
        pw = request.form['password']

        users = list_users()

        if name in users:
            return redirect(request.url)
    else:
        if 'name' in session:
            return 'Hello ' + escape(session['name'])
        else:
            return '''
                <form method="post">
                    <p><input type=text name="name" placeholder="Username">
                    <p><input type=password name="password" placeholder="Password">
                    <p><input type=submit value=Login>
                </form>
            
            '''


# Route for logout
@login_bp.route('/logout')
def logout():
    session.pop('name', None)
    return redirect(url_for('login.user_login'))
