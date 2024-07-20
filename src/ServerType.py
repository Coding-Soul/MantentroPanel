import json

class ServerType:
    def __int__(self, name, configuration : dict):
        self.name = name
        self.config = configuration