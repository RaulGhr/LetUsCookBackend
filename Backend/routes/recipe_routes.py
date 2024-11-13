from flask import Blueprint, request, jsonify
from services.recipe_service import RecipeService

recipe_bp = Blueprint('recipe_bp', __name__)

@recipe_bp.route('/create', methods=['POST'])
def create_recipe():
    data = request.get_json()
    user_id = data.get('user_id')
    title = data.get('title')
    images = data.get('images')
    description = data.get('description')
    instructions = data.get('instructions')
    servings = data.get('servings')
    prep_time = data.get('prep_time')
    cook_time = data.get('cook_time')

    recipe = RecipeService.add_recipe(user_id, title, images, description, instructions, servings, prep_time, cook_time)
    return jsonify({"message": "Recipe created successfully", "recipe": recipe.id}), 201

@recipe_bp.route('/getAll', methods=['GET'])
def get_all_recipes():
    recipes = RecipeService.get_all_recipes()
    return jsonify([recipe.to_dict() for recipe in recipes]), 200
