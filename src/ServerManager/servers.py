from src.ServerManager.server_manager import ServerManager
from src.ServerManager.server_type import ServerType

manager = ServerManager()

manager.add_server_type('Pycord', {})

print(manager.list_server_names())