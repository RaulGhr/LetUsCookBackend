from extensions import db
from models.recipe_like import RecipeLike
from repositories.recipe_like_repository import RecipeLikeRepository

class RecipeLikeService():

    @staticmethod
    def add_like(user_id, recipe_id):
        like = RecipeLike(user_id=user_id, recipe_id=recipe_id)
        RecipeLikeRepository.add_like(like)
        return like

    @staticmethod
    def delete_like(user_id, recipe_id):
        like = RecipeLike.query.filter_by(user_id=user_id, recipe_id=recipe_id).first()
        RecipeLikeRepository.delete_like(like)
        return like

    @staticmethod
    def get_like_by_ids(user_id, recipe_id):
        return RecipeLikeRepository.get_like_by_ids(user_id, recipe_id)

    @staticmethod
    def get_like_by_user_id(user_id):
        return RecipeLikeRepository.get_like_by_user_id(user_id)

    @staticmethod
    def get_like_by_recipe_id(recipe_id):
        return RecipeLikeRepository.get_like_by_recipe_id(recipe_id)

    @staticmethod
    def get_recipe_like_count(recipe_id):
        return RecipeLike.query.filter_by(recipe_id=recipe_id).count()

    @staticmethod
    def is_recipe_liked_by_user(user_id, recipe_id):
        return RecipeLikeRepository.get_like_by_ids(user_id, recipe_id) is not None