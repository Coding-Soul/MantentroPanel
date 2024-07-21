import sqlite3

PATH = 'users.db'


def create_user(username, email, password):
    conn = sqlite3.connect(PATH)