from flask import Blueprint
from flask import jsonify, request

from api.services import user_service

user = Blueprint('user', __name__)


@user.route('/user', methods=['POST'])
def save_user():
    request_data = request.get_json()
    is_saved: bool = user_service.save_user(request_data)
    if not is_saved:
        return jsonify({'message': 'User not saved'}), 400
    return jsonify({'message': 'User saved'}), 200


@user.route('/user', methods=['GET'])
def get_all_users():
    users = user_service.get_all_users()
    return jsonify({'users': [user.to_dict(only=('id', 'name', 'email', 'hashed_password', 'created_date')) for user in users]}), 200
