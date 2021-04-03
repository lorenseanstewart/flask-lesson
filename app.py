from flask import make_response, request, jsonify

from models import User
from startup import app, db
from utils import serialize_single, serialize_list


@app.route("/users", methods=["GET", "POST"])
def users():
    if request.method == "GET":
        queryset = db.session.query(User).all()
        serialized_data = serialize_list(queryset)
        return jsonify(serialized_data)
    else:
        # this is the POST route
        data = request.get_json()
        new_user = User(
            username=data.get("username"),
            email=data.get("email"),
            bio=data.get("bio"),
            admin=data.get("admin"),
        )
        db.session.add(new_user)  # Adds new User record to database
        db.session.commit()  # Commits all changes
        db.session.refresh(new_user)
        serialized_data = serialize_single(new_user)
        return jsonify(serialized_data)


@app.route("/users/<int:user_id>", methods=["GET", "POST"])
def user(user_id):
    queried_user = db.session.query(User).filter(id=user_id).first()
    print(queried_user)
    serialized_data = serialize_single(queried_user)
    return jsonify(serialized_data)
