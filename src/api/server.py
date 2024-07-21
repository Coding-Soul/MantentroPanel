from flask import Flask
from src.ServerManager import servers

# Route imports
from src.api.routes.home import home_bp

app = Flask(__name__)  # Creating flask instance


# Route for the list of all server types
@app.route('/api/server/types')
def server_types():
    return str(servers.manager.list_server_names())


# Route for creating a new server
@app.route('/api/server/create')
def create_server():
    return 'test'


app.register_blueprint(home_bp)


# Start function
def start(port: int, host: str, debug: bool):
    print('Starting api on ' + host + ':' + str(port) + ' with debugging ' + str(debug))  # logging
    app.run(port=port, debug=debug)  # running app
