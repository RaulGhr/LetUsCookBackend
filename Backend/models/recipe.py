from app import db
from models.user import User

class Recipe(db.Model):
    __tablename__ = 'Recipe'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id))
    title = db.Column(db.String(255), nullable=False)
    images = db.Column(db.Text)
    description = db.Column(db.Text)
    instructions = db.Column(db.JSON)
    servings = db.Column(db.Integer)
    prep_time = db.Column(db.Integer)
    cook_time = db.Column(db.Integer)
    number_of_likes = db.Column(db.Integer)
    ingredients = db.relationship('Ingredient', secondary='RecipeIngredient', back_populates='recipes')

    def like(self):
        self.number_of_likes += 1

    def dislike(self):
        self.number_of_likes -= 1

    def to_dict(self):
        return {"id": self.id,
                "userId": self.user_id,
                "title": self.title,
                "images": self.images,
                "description": self.description,
                "instructions": self.instructions,
                "servings": self.servings,
                "prepTime": self.prep_time,
                "cookTime": self.cook_time,
                "numberOfLikes": self.number_of_likes,
                "ingredients": [ingredient.to_dict() for ingredient in self.ingredients]
                }