import sqlite3

PATH = 'users.db'


def create_user(username, email, password):
    conn = sqlite3.connect(PATH)
    cursor = conn.cursor()

    try:
        cursor.execute('''
            INSERT INTO users (username, email, password)
            VALUES (?,?,?)
        
        ''', (username, email, password))
        conn.commit()
        print(username + " was successfully created!")
        return 0
    except sqlite3.IntegrityError:
        print('Error: Username must be unique')
        return 1
    finally:
        conn.close()