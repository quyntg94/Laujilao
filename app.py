from flask import Flask
from flask_restful import Resource, Api, reqparse
import json
import codecs
import os


APP_ROOT = os.path.dirname(os.path.abspath(__file__))
GUESTHOUSE_PATH = os.path.join(APP_ROOT, "guesthouse.json")

app = Flask(__name__)
api = Api(app)

class GuesthouseListRes(Resource):
    def get(self):
        with codecs.open(GUESTHOUSE_PATH, 'r', 'utf-8-sig') as data_file:
            return json.load(data_file)

api.add_resource(GuesthouseListRes, "/api/guesthouse")

if __name__ == '__main__':
    app.run()
