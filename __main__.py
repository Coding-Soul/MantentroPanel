from src.api import server

if __name__ == "__main__":
    api = server.start(port=1337, host='', debug=True)