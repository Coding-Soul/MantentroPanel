from server_type import ServerType


class ServerManager:
    def __int__(self):
        self.servers = []

    def add_server(self, server_type: ServerType):
        server = server_type
        self.servers.append(server)

    def get_config(self):
        pass
