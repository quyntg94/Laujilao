from flask import Flask
from flask_restful import Resource, Api, reqparse
import json
import codecs
import os

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
FOOD_PATH = os.path.join(APP_ROOT, "food.json")

app = Flask(__name__)
api = Api(app)

class FoodListRes(Resource):
    def get(self):
        with codecs.open(FOOD_PATH, 'r', 'utf-8-sig') as data_file:
            return json.load(data_file)

api.add_resource(FoodListRes, "/api/food")

if __name__ == '__main__':
    app.run()
