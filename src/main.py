from api import server
import user.setup


if __name__ == '__main__':
    user.database.create_db()
    api = server.start(port=1337, host='', debug=True)