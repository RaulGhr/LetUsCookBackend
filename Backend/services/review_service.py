from repositories.review_repository import ReviewRepository
from models.review import Review

class ReviewService:
    @staticmethod
    def add_review(user_id, recipe_id, comment):
        review = Review(user_id=user_id, recipe_id=recipe_id, comment=comment)
        ReviewRepository.add_review(review)
        return review

    @staticmethod
    def like_review(review_id):
        return ReviewRepository.like_review(review_id)

    @staticmethod
    def dislike_review(review_id):
        return ReviewRepository.dislike_review(review_id)
