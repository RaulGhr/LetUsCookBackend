from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from services.user_follow_service import UserFollowService

user_follow_bp = Blueprint('user_follow_bp', __name__)

@user_follow_bp.route('/follow', methods=['POST'])
@jwt_required()
def follow_user():
    data = request.get_json()
    followed_user_id = data.get('followed_user_id')
    follower_user_id = get_jwt_identity()

    try:
        UserFollowService.follow_user(follower_user_id, followed_user_id)
        return jsonify({"message": "User followed successfully"}), 201
    except ValueError as e:
        return jsonify({"message": str(e)}), 400

@user_follow_bp.route('/unfollow', methods=['POST'])
@jwt_required()
def unfollow_user():
    data = request.get_json()
    followed_user_id = data.get('followed_user_id')
    follower_user_id = get_jwt_identity()


    try:
        UserFollowService.unfollow_user(follower_user_id, followed_user_id)
        return jsonify({"message": "User unfollowed successfully"}), 200
    except ValueError as e:
        return jsonify({"message": str(e)}), 400

@user_follow_bp.route('/following_count/<int:user_id>', methods=['GET'])
def get_following_count(user_id):
    try:
        count = UserFollowService.get_following_count(user_id)
        return jsonify({"following_count": count}), 200
    except ValueError as e:
        return jsonify({"message": str(e)}), 400

@user_follow_bp.route('/follower_count/<int:user_id>', methods=['GET'])
def get_follower_count(user_id):
    try:
        count = UserFollowService.get_follower_count(user_id)
        return jsonify({"follower_count": count}), 200
    except ValueError as e:
        return jsonify({"message": str(e)}), 400

@user_follow_bp.route('/is_following', methods=['GET'])
@jwt_required()
def is_following():
    follower_user_id = get_jwt_identity()
    followed_user_id = request.args.get('user_id')

    return jsonify({"is_following": UserFollowService.is_following(follower_user_id, followed_user_id)}), 200

