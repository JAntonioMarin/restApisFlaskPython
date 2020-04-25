# create_table.py creation

import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY int, username text, password text)"
cursor.execute(create_table)

connection.commit()
connection.close()

# user.py

# import sqlite3
from flask_restful import Resource, reqparse


class User:
    pass

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True, help="This field cannot be blank.")
    parser.add_argument('password', type=str, required=True, help="This field cannot be blank.")

    def post(self):
        data = UserRegister.parser.parse_args()

        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "INSERT INTO users VALUE(NULL, ?,?)"
        cursor.execute(data['username'], data['password'])

        connection.commit()
        connection.close()

        return {"message": "User created sucessfully."}, 201


# app.py
from user import UserRegister

api.add_resource(UserRegister, '/register')
