from flask import Flask
from src.ServerManager import servers

app = Flask(__name__)


@app.route('/')
def home():
    return 'Flask is running'


# List of all server types
@app.route('/api/server/types')
def server_types():
    return str(servers.manager.list_server_names())


def start(port: int, host: str, debug: bool):
    print('Starting api on ' + host + ':' + str(port) + ' with debugging ' + str(debug))
    app.run(port=port, debug=debug)
