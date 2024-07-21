from flask import Flask

# Route imports
from src.api.routes.home import home_bp
from src.api.routes.servers import servers_bp
from src.api.routes.users import users_bp


app = Flask(__name__)  # Creating flask instance


# Routes register
app.register_blueprint(home_bp)
app.register_blueprint(servers_bp)
app.register_blueprint(users_bp)


# Start function
def start(port: int, host: str, debug: bool):
    print('Starting api on ' + host + ':' + str(port) + ' with debugging ' + str(debug))  # logging
    app.run(port=port, debug=debug)  # running app
