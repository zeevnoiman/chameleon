from flask import Blueprint, jsonify, request
from routes.words import words_blueprint
from routes.users import users_blueprint

api_blueprint = Blueprint('api', __name__)
api_blueprint.register_blueprint(words_blueprint, url_prefix='/words')
api_blueprint.register_blueprint(users_blueprint, url_prefix='/users')
