from flask import Flask
from src.config.Reader import read_config

# Route imports
from src.api.routes.home import home_bp
from src.api.routes.servers import servers_bp
from src.api.routes.users import users_bp
from src.api.routes.login import login_bp

app = Flask(__name__)  # Creating flask instance

# Routes register
app.register_blueprint(home_bp)
app.register_blueprint(servers_bp)
app.register_blueprint(users_bp)
app.register_blueprint(login_bp)

app.secret_key = read_config('key')


# Start function
def start(port: int, host: str, debug: bool):
    print('Starting api on ' + host + ':' + str(port) + ' with debugging ' + str(debug))  # logging
    app.run(port=port, debug=debug)  # running app
