from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
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
        access_token = create_access_token(identity=user.id)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"message": "Invalid credentials"}), 401

