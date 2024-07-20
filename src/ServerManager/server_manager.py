from src.ServerManager.server_type import ServerType


class ServerManager:
    def __init__(self):
        self.servers = []

    def add_server(self, name: str, configuration:dict):
        server = ServerType(name=name, configuration=configuration)
        self.servers.append(server)

    def list_server_names(self):
        for server in self.servers:
            return server.name

    def get_config(self):
        pass
