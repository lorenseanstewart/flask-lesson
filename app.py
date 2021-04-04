from flask import make_response, request, jsonify

from models import User
from startup import app, db
from utils import serialize_single, serialize_list


# make a route that can (1) get all users or (2) create a new user

@app.route('/users', methods=['GET'])
def users():
    if request.method == 'GET':
        return jsonify('got it!')

# create a route that gets a single user by id
