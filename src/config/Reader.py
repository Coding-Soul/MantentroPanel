import json


def read_config(arg):
    with open('Z:\Coding\Projekte\Coding Soul\MantentroPanel\src\config\secret_key.json') as f:
        return json.load(f)[arg]
