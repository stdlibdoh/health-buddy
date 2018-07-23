from flask import jsonify, request
from app import db
from app.models import User
from app.api import bp


@bp.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json(force=True) or {}
    user = User()
    user.from_dict(data)
    db.session.add(user)
    db.session.commit()
    response = jsonify(user.to_dict())
    response.status_code = 201
    return response


@bp.route('/get_user/<phone_no>', methods=['GET'])
def get_user(phone_no):
    user = User.query.filter_by(phone_no=phone_no).first()
    response = jsonify(user.to_dict())
    response.status_code = 200
    return response


@bp.route('/get_all', methods=['GET'])
def get_all():
    users = User.to_collection_dict(User.query)
    response = jsonify(users)
    response.status_code = 201
    return response


# NOT NEEDED ?
@bp.route('/edit_user', methods=['PUT'])
def edit_user():
    return "EDITED"


@bp.route('/del_user/<phone_no>', methods=['DELETE'])
def del_user(phone_no):
    user = User.query.filter_by(phone_no=phone_no).first()
    db.session.delete(user)
    db.session.commit()
    response = jsonify("User deleted")
    response.status_code = 202
    return response

