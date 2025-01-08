from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from services.review_service import ReviewService
from services.user_service import UserService

review_bp = Blueprint('review_bp', __name__)

@review_bp.route('/create', methods=['POST'])
@jwt_required()
def create_review():
    data = request.get_json()
    user_id = get_jwt_identity()
    recipe_id = data.get('recipe_id')
    comment = data.get('comment')

    review = ReviewService.add_review(user_id, recipe_id, comment)
    return jsonify({"message": "Review created successfully", "review": review.to_dict()}), 201

@review_bp.route('/getByRecipe', methods=['GET'])
def get_reviews_by_recipe():
    recipe_id = request.args.get('recipe_id')
    reviews = ReviewService.get_reviews_by_recipe(recipe_id)
    review_json = [review.to_dict() for review in reviews]
    for review in review_json:
        user = UserService.get_user_by_id(review['user_id'])
        review['username'] = user.username

    return jsonify(review_json), 200

@review_bp.route('/like', methods=['PUT'])
def like_review():
    data = request.get_json()
    review_id = data.get('review_id')
    review = ReviewService.like_review(review_id)
    if review:
        return jsonify({"message": "Review liked successfully", "review": review.to_dict()}), 200
    else:
        return jsonify({"message": "Review not found"}), 404

@review_bp.route('/dislike', methods=['PUT'])
def dislike_review():
    data = request.get_json()
    review_id = data.get('review_id')
    review = ReviewService.dislike_review(review_id)
    if review:
        return jsonify({"message": "Review disliked successfully", "review": review.to_dict()}), 200
    else:
        return jsonify({"message": "Review not found"}), 404