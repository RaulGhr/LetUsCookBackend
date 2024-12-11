from models.review import Review
from extensions import db

class ReviewRepository:
    @staticmethod
    def add_review(review):
        db.session.add(review)
        db.session.commit()

    @staticmethod
    def get_review_by_id(review_id):
        return Review.query.get(review_id)

    @staticmethod
    def like_review(review_id):
        review = Review.query.get(review_id)
        if review:
            review.number_of_likes += 1
            db.session.commit()
        return review

    @staticmethod
    def dislike_review(review_id):
        review = Review.query.get(review_id)
        if review:
            review.number_of_dislikes += 1
            db.session.commit()
        return review
