# pip3 install Flask-JWT

from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
app.secret_key = 'test'
api = Api(app)

items = []


class Item(Resource):
    def get(self, name):
        item = next(filter(lambda x: x['name'] == name, items), None)
        return {'name': item}, 200 if item else 404

    def post(self, name):
        if next(filter(lambda x: x['name'] == name, items), None) is not None:
            return {'message': "An item with name '{}' already exists.".format(name)}, 400

        data = request.get_json(force=True)
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201  # 201 CREATED

class ItemList(Resource):
    def get(self):
        return {'items': items}

api.add_resource(Item, '/item/<string:name>')  # http://127.0.0.1:5000/item/
api.add_resource(ItemList, '/items')

app.run(port=5000, debug=True)