import sqlite3


def delete(self, name):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    query = "DELETE FROM items WHERE name=?"
    cursor.execute(query, (name,))

    connection.commit()
    connection.close()

    return {'message': 'Item deleted'}
