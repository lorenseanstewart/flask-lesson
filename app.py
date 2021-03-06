from flask import make_response, request, jsonify

from models import User
from startup import app, db
from utils import serialize_single, serialize_list


# make a route that can (1) get all users or (2) create a new user

@app.route('/users', methods=['GET', 'POST'])
def users():
    if request.method == 'GET':
        query_set = db.session.query(User).all()
        serialized_data = serialize_list(query_set)
        return jsonify(serialized_data)
    else:
        data = request.get_json()
        new_user = User(
            username=data.get("username"),
            email=data.get("email"),
            bio=data.get("bio"),
            admin=data.get("admin"),
        )
        db.session.add(new_user)
        db.session.commit()
        db.session.refresh(new_user)
        serialized_data = serialize_single(new_user)
        return jsonify(serialized_data)

@app.route("/users/<int:user_id>", methods=["GET"])
def user(user_id):
    query_set = db.session.query(User).get(user_id)
    if query_set:
        serialized_data = serialize_single(query_set)
        return jsonify(serialized_data)
    else:
        return jsonify(f'User with id {user_id} not found')

# create a route that gets a single user by id
