from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from services.recipe_service import RecipeService

recipe_bp = Blueprint('recipe_bp', __name__)

@recipe_bp.route('/create', methods=['POST'])
@jwt_required()
def create_recipe():
    data = request.get_json()
    user_id = get_jwt_identity()
    title = data.get('title')
    images = data.get('img')
    description = data.get('description')
    instructions = data.get('instructions')
    servings = data.get('servings')
    prep_time = data.get('preptime')
    cook_time = data.get('cooktime')
    ingredients = data.get('ingredients')

    service_result = RecipeService.add_recipe(user_id, title, images, description, instructions, servings, prep_time, cook_time, ingredients)
    if not service_result.success:
        return jsonify(service_result.get_error_map()), service_result.status_code

    return jsonify(service_result.data.to_dict()), service_result.status_code

@recipe_bp.route('/', methods=['GET'])
@jwt_required()
def get_all_recipes():
    query_params = request.args
    title = query_params.get('title')

    recipes = RecipeService.get_all_recipes(title)
    return jsonify([recipe.to_dict() for recipe in recipes]), 200

@recipe_bp.route('/getAllForUser', methods=['GET'])
@jwt_required()
def get_all_recipes_for_user():
    user_id = get_jwt_identity()
    recipes = RecipeService.get_recipes_by_user_id(user_id)
    return jsonify([recipe.to_dict() for recipe in recipes]), 200

@recipe_bp.route('/<int:recipe_id>/like', methods=['POST'])
@jwt_required()
def like_recipe(recipe_id):
    service_result = RecipeService.like_recipe(recipe_id)
    if not service_result.success:
        return jsonify(service_result.get_error_map()), service_result.status_code

    return '', 200

@recipe_bp.route('/<int:recipe_id>/dislike', methods=['POST'])
@jwt_required()
def dislike_recipe(recipe_id):
    service_result = RecipeService.dislike_recipe(recipe_id)
    if not service_result.success:
        return jsonify(service_result.get_error_map()), service_result.status_code

    return '', 200

