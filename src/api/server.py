from flask import Flask
from src.ServerManager import servers

app = Flask(__name__)  # Creating flask instance


# Home Directory
@app.route('/')
def home():
    return 'Flask is running'


# Route for the list of all server types
@app.route('/api/server/types')
def server_types():
    return str(servers.manager.list_server_names())


# Route for creating a new server
@app.route('/api/server/create')
def create_server():
    return 'test'


# Start function
def start(port: int, host: str, debug: bool):
    print('Starting api on ' + host + ':' + str(port) + ' with debugging ' + str(debug))  # logging
    app.run(port=port, debug=debug)  # running app
