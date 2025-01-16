from models.recipe_like import RecipeLike
from extensions import db

class RecipeLikeRepository():

    @staticmethod
    def add_like(like):
        db.session.add(like)
        db.session.commit()

    @staticmethod
    def delete_like(like):
        db.session.delete(like)
        db.session.commit()

    @staticmethod
    def get_like_by_ids(user_id, recipe_id):
        return RecipeLike.query.filter_by(user_id=user_id, recipe_id=recipe_id).first()

    @staticmethod
    def get_like_by_user_id(user_id):
        return RecipeLike.query.filter_by(user_id=user_id).all()

    @staticmethod
    def get_like_by_recipe_id(recipe_id):
        return RecipeLike.query.filter_by(recipe_id=recipe_id).all()