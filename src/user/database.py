import sqlite3

PATH = 'user.db'


# to set the database up
def create_db(self):
    conn = sqlite3.connect(self.path)
    cursor = conn.cursor()

    # Creating table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
            )
    ''')

    conn.commit()
    conn.close()
