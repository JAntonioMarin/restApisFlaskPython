import sqlite3
from werkzeug.security import safe_str_cmp


class User:
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE username=?"
        result = cursor.execute(query, (username,)) # individual value is (value,) like 5+3*8 or (5+3)*8
        row = result.fetchone()
        if row:
            # user = User(row[0], row[1], row[2])
            user = cls(*row)
        else:
            user = None

        connection.close()
        return user

    @classmethod
    def find_by_id(cls, _id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE id=?"
        result = cursor.execute(query, (_id,)) # individual value is (value,) like 5+3*8 or (5+3)*8
        row = result.fetchone()
        if row:
            # user = User(row[0], row[1], row[2])
            user = cls(*row)
        else:
            user = None

        connection.close()
        return user

def identity(payload):
    user_id = payload['identity']
    return User.find_by_id(user_id)

