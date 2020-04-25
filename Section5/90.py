# app.py

if __name__ == '__main__':
    app.run(port=5000, debuf=True)

# item.py
import sqlite3


@jwt_required()
def get(self, name):
    item = self.find_by_name(name)
    if item:
        return item
    return {'message': 'Item not found'}, 404


@classmethod
def find_by_name(cls, name):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    query = "SELECT * FROM {table} WHERE name=?".format(table=cls.TABLE_NAME)
    result = cursor.execute(query, (name,))
    row = result.fetchone()
    connection.close()

    if row:
        return {'item': {'name': row[0], 'price': row[1]}}


def post(self, name):
    if self.find_by_name(name):
        return {'message': "An item with name '{}' already exists".format(name)}, 400

    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    query = "INSERT INTO items value (?,?)"
    cursor.execute(query, (item['name'], item['price']))
