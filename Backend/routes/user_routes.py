from datetime import timedelta

from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token

from app import app
from services.user_service import UserService

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    user = UserService.create_user(username, email, password)
    return jsonify({"message": "User created successfully", "user": user.id}), 201

@user_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user = UserService.get_user_by_email(email)

    if user and UserService.check_password(user, password):
        expiry_time = timedelta(minutes=app.config['JWT_EXPIRY_MINUTES'])
        access_token = create_access_token(identity=user.id, expires_delta=expiry_time)
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
        return jsonify({"message": "No username provided"}), 400

    users = UserService.filter_users_by_username(username)
    return jsonify([{
        "id": user.id,
        "username": user.username,
        "email": user.email,
        "profileImage": user.profileImage,
        "description": user.description
    }for user in users]), 200