from flask import Flask
from ..ServerManager import servers


app = Flask(__name__)


@app.route('/')
def home():
    return 'Flask is working!'


@app.route('/api/server/types')
def server_types():
    return str(servers.server_types)


def start(port: int, host: str, debug: bool):
    app.run(port=port, debug=debug)
