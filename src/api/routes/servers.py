from flask import Blueprint
from src.ServerManager import servers

servers_bp = Blueprint('servers', __name__)


# Route for the list of all server types
@servers_bp.route('/api/server/types')
def server_types():
    return str(servers.manager.list_server_names())


# Route for creating a new server
@servers_bp.route('/api/server/create')
def create_server():
    return 'test'
