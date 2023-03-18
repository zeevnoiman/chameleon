from flask import Blueprint, jsonify, request

users_blueprint = Blueprint('users', __name__)

@users_blueprint.route('/', methods=['GET'])
def get_users():
    return jsonify({'users': ['hello', 'world']})