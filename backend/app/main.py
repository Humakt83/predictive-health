from datetime import datetime
from random import randrange
from numpy import log as ln
import json
from bson import ObjectId
from flask import Flask, g, request, redirect, url_for, jsonify, Response, abort
from flask_pymongo import PyMongo
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config["MONGO_URI"] = "mongodb://mongodb:27017/user"
mongo = PyMongo(app)

# Because ObjectId can not be json serialized
class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)
        
def find(json_object, name):
    #for dict in json_object['answers']:
    #    if dict['name'] == name:
    #        return dict['optionValue']
    return [obj for obj in json_object['answers'] if obj['name']==name][0]['optionValue']
    
# Returns true when factor > 0.5
def Logit(factor):
    return bool(ln(factor / (1 - factor)) > 0.0)

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
    poll = all_poll.find_one({'user': user_id })
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
    poll_id = all_poll.insert(data)
    user_poll = all_poll.find_one({'_id': poll_id })

    return JSONEncoder().encode(user_poll)

# Get user prediction
@app.route("/user/<string:user_id>/prediction", methods=["GET"])
#@login_required
def user_prediction(user_id):
    all_poll = mongo.db.poll
    poll = all_poll.find_one({'user': user_id })

    Random = randrange(4)

    Yogurt_Kefir = find(poll, 'Yoghurt/Kefir')
    SweetenedBeverages = find(poll, 'Sweetened Beverages')
    Fruits = find(poll, 'Fruits')
    RefinedCerials = find(poll, 'Refined Cereals')
    Milk_Cheese = find(poll, 'Milk/Cheese')
    RedProcessedMeat = find(poll, 'Red/Processed Meat')
    Tea_Coffee = find(poll, 'Tea/Coffee')
    WholeGrain = find(poll, 'Whole-grain')
    Eggs = find(poll, 'Eggs')
    Vegetables = find(poll, 'Vegetables')
    Fish = find(poll, 'Fish')
    Nuts = find(poll, 'Nuts/Seeds')
    Legumes = find(poll, 'Legumes')
    
    t2d = -509.30+44.37*Yogurt_Kefir+44.14*SweetenedBeverages+44.36*Fruits+44.24*RefinedCerials+44.30*Random
    ibd = -988.890+42.34*Milk_Cheese+42.11*Yogurt_Kefir+42.26*RedProcessedMeat+42.17*Tea_Coffee+41.86*SweetenedBeverages+41.88*WholeGrain+41.76*RefinedCerials+42.26*Eggs+42.09 * Random
    ha = -246.05+44.75*RedProcessedMeat+44.73*Eggs+44.79*Random
    cc = -509.76+44.41*Yogurt_Kefir+44.38*RedProcessedMeat+44.26*SweetenedBeverages+44.25*RefinedCerials+44.35*Random

    data = {}
    data['t2d'] = Logit(t2d)
    data['ibd'] = Logit(ibd)
    data['ha'] = Logit(ha)
    data['cc'] = Logit(cc)
    
    if user is not None:
        return json.dumps(data)
    else:
        abort(404, 'user not found')


if __name__ == "__main__":
    app.config.update(
        DEBUG = True
    )
    # Only for debugging while developing    
    app.run(host='0.0.0.0', debug=True, port=80)