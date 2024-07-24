import sqlite3
import argon2

PATH = 'Z:/Coding/Projekte/Coding Soul/MantentroPanel/src/user/users.db'


# Creating user
def create_user(username: str, email: str, password: str):
    conn = sqlite3.connect(PATH)
    cursor = conn.cursor()

    try:
        cursor.execute('''
            INSERT INTO users (username, email, password)
            VALUES (?,?,?)
        ''', (username, email, hash_password(password)))
        conn.commit()
        print(username + " was successfully created!")
        result = {'status': 'success', 'message': f'User created: {username}'}
    except sqlite3.IntegrityError:
        print('Error: Username must be unique')
        result = {'status': 'error', 'message': f'Error while creating user.'}
    finally:
        conn.close()
        return result


def hash_password(password):
    ph = argon2.PasswordHasher()
    return ph.hash(password)


def verify_password(stored_password, entered_password):
    ph = argon2.PasswordHasher()

    try:
        ph.verify(stored_password, entered_password)
        return True

    except argon2.exceptions.VerifyMismatchError:
        return False


# User list
def list_users():
    conn = sqlite3.connect(PATH)
    cursor = conn.cursor()

    cursor.execute('SELECT id, username, email, password FROM users')
    users = cursor.fetchall()

    output = {}

    for user in users:
        output[user[0]] = {user[1]: [user[3]]}

    conn.close()
    print(output)
    return output



# Deleting user function
def delete_user(user_id):
    conn = sqlite3.connect(PATH)
    cursor = conn.cursor()

    cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))
    if cursor.rowcount > 0:
        conn.commit()
        print(f'User with the user-id {user_id} was deleted')
        result = {'status': 'success', 'message': f'User with the user-id {user_id} was deleted!'}
    else:
        print('Error, while deleting User')
        result = {'status': 'error', 'message': 'Error, while deleting User'}

    conn.close()
    return result
