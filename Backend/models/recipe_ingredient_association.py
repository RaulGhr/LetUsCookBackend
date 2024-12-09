from app import db

recipe_ingredient = db.Table(
    'RecipeIngredient',
    db.Column('recipe_id', db.Integer, db.ForeignKey('Recipe.id'), primary_key=True),
    db.Column('ingredient_id', db.Integer, db.ForeignKey('Ingredient.id'), primary_key=True)
)
