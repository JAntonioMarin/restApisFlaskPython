# pip3 install Flask-JWT

from flask import Flask, request
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required

from security import authenticate, identity

app = Flask(__name__)
app.secret_key = 'test'



jwt = JWT(app, authenticate, identity) # /auth

items = []


class Item(Resource):
    @jwt_required() # postman error in json post to jwt, but u can use rested (mozilla extension)
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

    def delete(self, name):
        global items
        items = list(filter(lambda x: x['name'] != name, items))
        return {'message': 'Item deleted'}


class ItemList(Resource):
    def get(self):
        return {'items': items}
api = Api(app)
api.add_resource(Item, '/item/<string:name>')  # http://127.0.0.1:5000/item/
api.add_resource(ItemList, '/items')

app.run(port=5000, debug=True)