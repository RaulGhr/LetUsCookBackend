from extensions import db

class Review(db.Model):
    __tablename__ = 'Review'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'), nullable=False)
    recipe_id = db.Column(db.Integer, db.ForeignKey('Recipe.id'), nullable=False)
    comment = db.Column(db.Text, nullable=False)
    number_of_likes = db.Column(db.Integer, default=0)
    number_of_dislikes = db.Column(db.Integer, default=0)

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "recipe_id": self.recipe_id,
            "comment": self.comment,
            "number_of_likes": self.number_of_likes,
            "number_of_dislikes": self.number_of_dislikes
        }