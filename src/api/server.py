from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return 'Flask is working!'


@app.route('/api/server/types')
def


def start(port: int, host: str, debug: bool):
    app.run(port=port, debug=debug)
