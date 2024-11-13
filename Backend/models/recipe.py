from app import db
from models.user import User
from models.ingredient import Ingredient

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

    def to_dict(self):
        return {"id": self.id,
                "user_id": self.user_id,
                "title": self.title,
                "images": self.images,
                "description": self.description,
                "instructions": self.instructions,
                "servings": self.servings,
                "prep_time": self.prep_time,
                "cook_time": self.cook_time
                }