
def put(self, name):
    data = Item.parser.parse_args()
    item = self.find_by_name(name)
    updated_item = {'name': name, 'price': data['price']}
    if item is None:
        try:
            Item.insert(updated_item)
        except:
            return {"message": "An error occurred inserting the item."}
    else:
        try:
            Item.update(updated_item)
        except:
            return {"message": "An error occurred updating the item."}
    return updated_item

@classmethod
def update(cls, item):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    query = "UPDATE {table} SET price=? WHERE name=?".format(table=cls.TABLE_NAME)
    cursor.execute(query, (item['price'], item['name']))

    connection.commit()
    connection.close()