import sqlite3

PATH = 'users.db'


# to set the database up
def create_db():
    print('Creating database...')
    conn = sqlite3.connect(PATH)
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
    print('Database connection closed!')


create_db()
