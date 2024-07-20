import json


class ServerType:
    def __int__(self, name: str, configuration: dict):
        self.name = name
        self.config = configuration
