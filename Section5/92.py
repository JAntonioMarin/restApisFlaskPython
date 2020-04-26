import sqlite3

@classmethod
def insert(cls, item):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    query = "INSERT INTO {table} VALUES(?, ?)".format(table=cls.TABLE_NAME)
    cursor.execute(query, (item['name'], item['price']))

    connection.commit()
    connection.close()

def post(self, name):

    '''

    '''
    try:
        self.insert(item)
    except:
        return {"An error ocurred inserting the item"}

    return item, 201
