from datetime import datetime
import json
from bson import ObjectId
from flask import Flask, g, request, redirect, url_for, jsonify, Response, abort

from flask_pymongo import PyMongo

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://mongodb:27017/user"
mongo = PyMongo(app)

# Because ObjectId can not be json serialized
class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)
# Get all users
@app.route("/users")
def users():
    allusers = mongo.db.user

    output = []
    for s in allusers.find():
        output.append(JSONEncoder().encode(s))

    return jsonify(output)

# Get user
@app.route("/user/<string:user_id>", methods=["GET"])
#@login_required
def user(user_id):
    allusers = mongo.db.user
    user = allusers.find_one({'_id': ObjectId(user_id) })
    if user is not None:
        return JSONEncoder().encode(user)
    else:
        abort(404, 'user not found')

# Add new user
@app.route("/user", methods=["POST"])
#@login_required
def create():
    allusers = mongo.db.user

    user_id = allusers.insert(request.json)

    new_user = allusers.find_one({'_id': user_id })

    return JSONEncoder().encode(new_user)

# Get user poll
@app.route("/user/<string:user_id>/poll", methods=["GET"])
#@login_required
def user_poll(user_id):
    all_poll = mongo.db.poll
    poll = all_poll.find_one({'user_id': ObjectId(user_id) })
    if user is not None:
        return JSONEncoder().encode(poll)
    else:
        abort(404, 'user not found')

# Add new user poll
@app.route("/user/<string:user_id>/poll", methods=["POST"])
#@login_required
def create_poll(user_id):
    all_poll = mongo.db.poll
    data = request.json
    data['user_id'] = ObjectId(user_id)
    poll_id = all_poll.insert(data)
    user_poll = all_poll.find_one({'_id': poll_id })

    return JSONEncoder().encode(user_poll)

# Get user prediction
@app.route("/user/<string:user_id>/prediction", methods=["GET"])
#@login_required
def user_prediction(user_id):
    all_poll = mongo.db.poll
    poll = all_poll.find_one({'user_id': ObjectId(user_id) })
    if user is not None:
        return JSONEncoder().encode(poll)
    else:
        abort(404, 'user not found')


if __name__ == "__main__":
    app.config.update(
        DEBUG = True
    )
    # Only for debugging while developing    
    app.run(host='0.0.0.0', debug=True, port=80)