from flask import Flask
from ..ServerManager import servers


app = Flask(__name__)


@app.route('/')
def home():
    return 'Flask is running'


@app.route('/api/server/types')
def server_types():
    return str(servers.server_types)


def start(port: int, host: str, debug: bool):
    print('Starting api on ' + host + ':' + str(port) + ' with debugging ' + str(debug))
    app.run(port=port, debug=debug)
