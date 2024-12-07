from models.user import User
from app import db

class UserRepository:
    @staticmethod
    def add_user(user):
        db.session.add(user)
        db.session.commit()

    @staticmethod
    def get_user_by_id(user_id):
        return User.query.get(user_id)

    @staticmethod
    def get_user_by_email(email):
        return User.query.filter_by(email=email).first()

    @staticmethod
    def update_user(user):
        db.session.commit()

    @staticmethod
    def filter_users_by_username(username):
        return User.query.filter(User.username.like(f'{username}%')).all()