from flask import Blueprint, request, session, redirect
from src.ServerManager import servers
from markupsafe import escape
import os

login_bp = Blueprint('login', __name__)


# Route for the list of all server types
@login_bp.route('/login', methods=['POST', 'GET'])
def server_types():
    if request.method == 'POST':
        session['name'] = request.form['name']
        return redirect(request.url)
    else:
        if 'name' in session:
            return 'Hello ' + escape(session['name'])
        else:
            return '''
                <form method="post">
                    <p><input type=text name="name">
                    <p><input type=submit value=Login>
                </form>
            
            '''


