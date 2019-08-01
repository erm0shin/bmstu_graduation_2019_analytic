import json
import datetime
from bson.objectid import ObjectId
from flask import Flask, request, jsonify
from flask_pymongo import PyMongo


class JSONEncoder(json.JSONEncoder):
    ''' extend json-encoder class'''

    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        if isinstance(o, datetime.datetime):
            return str(o)
        return json.JSONEncoder.default(self, o)


app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/bmstu_graduation"
mongo = PyMongo(app)

# use the modified encoder class to handle ObjectId & datetime object while jsonifying the response.
app.json_encoder = JSONEncoder


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/performance')
def get_all_performance():
    data = mongo.db.performance.find_one()
    return jsonify(data), 200


if __name__ == '__main__':
    app.run()
