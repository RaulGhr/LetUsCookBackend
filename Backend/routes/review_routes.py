from flask import Blueprint, request, jsonify
from services.review_service import ReviewService

review_bp = Blueprint('review_bp', __name__)

@review_bp.route('/create', methods=['POST'])
def create_review():
    data = request.get_json()
    user_id = data.get('user_id')
    recipe_id = data.get('recipe_id')
    comment = data.get('comment')

    review = ReviewService.add_review(user_id, recipe_id, comment)
    return jsonify({"message": "Review created successfully", "review": review.to_dict()}), 201

@review_bp.route('/like/<int:review_id>', methods=['POST'])
def like_review(review_id):
    review = ReviewService.like_review(review_id)
    if review:
        return jsonify({"message": "Review liked successfully", "review": review.to_dict()}), 200
    else:
        return jsonify({"message": "Review not found"}), 404

@review_bp.route('/dislike/<int:review_id>', methods=['POST'])
def dislike_review(review_id):
    review = ReviewService.dislike_review(review_id)
    if review:
        return jsonify({"message": "Review disliked successfully", "review": review.to_dict()}), 200
    else:
        return jsonify({"message": "Review not found"}), 404