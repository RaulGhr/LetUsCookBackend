from flask import Blueprint, request, jsonify

from services.favorite_recipe_service import FavoriteRecipeService

favorite_recipe_bp = Blueprint('favorite_recipe_bp', __name__)

@favorite_recipe_bp.route('/create', methods=['POST'])
def create_favorite_recipe():
    body = request.get_json()
    user_id = body['user_id']
    recipe_id = body['recipe_id']

    favorite_recipe = FavoriteRecipeService.add_favorite_recipe(user_id, recipe_id)
    return jsonify({"message": "Favorite Recipe added successfully", "favorite_recipe": favorite_recipe.id}), 201

@favorite_recipe_bp.route('/getAll', methods=['GET'])
def get_all_favorite_recipes():
    favorite_recipes = FavoriteRecipeService.get_all_favorite_recipes()
    return jsonify([favorite_recipe.to_dict() for favorite_recipe in favorite_recipes]), 200

@favorite_recipe_bp.route('/getFavoriteRecipeByUserId/<int:user_id>', methods=['GET'])
def get_favorite_recipe_by_user_id(user_id):
    user_favorite_recipes = FavoriteRecipeService.get_favorite_recipe_by_user_id(user_id)
    return jsonify([favorite_recipe.to_dict() for favorite_recipe in user_favorite_recipes]), 200