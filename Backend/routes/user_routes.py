from datetime import timedelta

import flask
from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity


from services.user_service import UserService
app = flask.current_app
user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    user = UserService.create_user(username, email, password)

    expiry_time = timedelta(minutes=app.config['JWT_EXPIRY_MINUTES'])
    access_token = create_access_token(identity=str(user.id), expires_delta=expiry_time)
    return jsonify(access_token=access_token), 201

@user_bp.route('/login', methods=['POST'])
def login():
    print("login")
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user = UserService.get_user_by_email(email)

    if user and UserService.check_password(user, password):
        expiry_time = timedelta(minutes=app.config['JWT_EXPIRY_MINUTES'])
        access_token = create_access_token(identity=str(user.id), expires_delta=expiry_time)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"message": "Invalid credentials"}), 401

@user_bp.route('/update_user/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    updated_user = UserService.update_user(user_id, data)

    if updated_user:
        return jsonify({
            "message": "User updated successfully",
            "user": {"id": updated_user.id,
                     "username": updated_user.username,
                     "email": updated_user.email,
                     "profileImage": updated_user.profileImage,
                     "description": updated_user.description
                     }
                }), 200
    return jsonify({"message": "User not found"}), 404

@user_bp.route('/filter', methods=['GET'])
def filter_users():
    username = request.args.get('username')
    if not username:
        username = ''

    users = UserService.filter_users_by_username(username)
    return jsonify([user.to_dict() for user in users]), 200

@user_bp.route('/profile', methods=['GET'])
@jwt_required()
def get_logged_in_user_details():
    user_id = get_jwt_identity()
    user = UserService.get_user_by_id(user_id)
    return jsonify(user.to_dict()), 200