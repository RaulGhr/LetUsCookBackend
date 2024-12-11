from extensions import db

class UserFollow(db.Model):
    __tablename__ = 'UserFollow'

    id = db.Column(db.Integer, primary_key=True)
    follower_user_id = db.Column(db.Integer, db.ForeignKey('User.id'), nullable=False)
    followed_user_id = db.Column(db.Integer, db.ForeignKey('User.id'), nullable=False)

    follower = db.relationship('User', foreign_keys=[follower_user_id], backref='following')
    followed = db.relationship('User', foreign_keys=[followed_user_id], backref='followers')
