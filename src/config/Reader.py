import json
import os


def read_config(arg):
    file_path = r'Z:\Coding\Projekte\Coding Soul\MantentroPanel\src\config\secret_key.json'

    try:
        with open(file_path, 'r') as f:
            return json.load(f)[arg]
    except FileNotFoundError:
        dictionary = {
            "key": f"{os.urandom(24)}"
        }
        with open(file_path, 'w') as f:
            json.dump(dictionary, f, ensure_ascii=False, indent=4)

        return dictionary[arg]