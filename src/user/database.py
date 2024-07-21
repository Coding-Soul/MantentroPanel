import sqlite3

PATH = 'Z:/Coding/Projekte/Coding Soul/MantentroPanel/src/user/users.db'


def create_user(username: str, email: str, password: str):
    conn = sqlite3.connect(PATH)
    cursor = conn.cursor()

    try:
        cursor.execute('''
            INSERT INTO users (username, email, password)
            VALUES (?,?,?)
        ''', (username, email, password))
        conn.commit()
        print(username + " was successfully created!")
    except sqlite3.IntegrityError:
        print('Error: Username must be unique')
    finally:
        conn.close()


def list_users():
    conn = sqlite3.connect(PATH)
    cursor = conn.cursor()

    cursor.execute('SELECT id, username, email FROM users')
    users = cursor.fetchall()

    output = ""

    print('Test')
    for user in users:
        print(f"Users: ID: {user[0]}, Username: {user[1]}, Email: {user[2]}")
        output += f"\nID: {user[0]}, Username: {user[1]}, Email: {user[2]}"

    conn.close()


