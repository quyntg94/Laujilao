from flask import Flask
from flask_restful import Resource, Api, reqparse
import json
import codecs
import os
import mlab
from mongoengine import *

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
FOOD_PATH = os.path.join(APP_ROOT, "food.json")

app = Flask(__name__)
api = Api(app)
mlab.connect()

parser = reqparse.RequestParser()
parser.add_argument("username", type=str, location="json", help="Username")
parser.add_argument("password", type=str, location="json", help="Password")

class Account(Document):
    username = StringField()
    password = StringField()

class AccountListRes(Resource):
    def get(self):
        return mlab.list2json(Account.objects)

    def post(self):
        args = parser.parse_args()

        username = args["username"]
        password = args["password"]

        account = Account(username=username,
                                password=password)
        account.save()

        return mlab.item2json(Account.objects().with_id(account.id))

class FoodListRes(Resource):
    def get(self):
        with codecs.open(FOOD_PATH, 'r', 'utf-8-sig') as data_file:
            return json.load(data_file)

api.add_resource(FoodListRes, "/api/food")
api.add_resource(AccountListRes, "/api/account")

if __name__ == '__main__':
    app.run()
