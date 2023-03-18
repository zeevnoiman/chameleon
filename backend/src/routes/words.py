from flask import Blueprint, jsonify, request

words_blueprint = Blueprint('words', __name__)

@words_blueprint.route('/', methods=['GET'])
def get_words():
    return jsonify({'words': ['hello', 'world']})