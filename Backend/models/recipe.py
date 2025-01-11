from extensions import db
from models.user import User
from datetime import datetime

class Recipe(db.Model):
    __tablename__ = 'Recipe'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id))
    user = db.relationship('User', back_populates='recipes')
    title = db.Column(db.String(255), nullable=False)
    images = db.Column(db.Text)
    description = db.Column(db.Text)
    instructions = db.Column(db.JSON)
    servings = db.Column(db.Integer)
    prep_time = db.Column(db.Integer)
    cook_time = db.Column(db.Integer)
    number_of_likes = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    recipe_ingredients = db.relationship(
        'RecipeIngredient',
        back_populates='recipe',
        overlaps="ingredients"
    )
    ingredients = db.relationship(
        'Ingredient',
        secondary='RecipeIngredient',
        back_populates='recipes',
        overlaps="recipe_ingredients"
    )

    def like(self):
        self.number_of_likes += 1

    def dislike(self):
        self.number_of_likes -= 1

    def to_dict(self):
        return {
            "id": self.id,
            "user": self.user.to_dict(),
            "title": self.title,
            "images": self.images,
            "description": self.description,
            "instructions": self.instructions,
            "servings": self.servings,
            "prepTime": self.prep_time,
            "cookTime": self.cook_time,
            "numberOfLikes": self.number_of_likes,
            "createdAt": self.created_at.isoformat(),
            "ingredients": [
                {
                    "ingredient": ingredient.to_dict(),
                    "quantity": ri.quantity
                }
                for ri in self.recipe_ingredients
                for ingredient in [ri.ingredient]
            ]
        }