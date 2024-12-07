from models.user_follow import UserFollow
from app import db

class UserFollowRepository:
    @staticmethod
    def follow_user(follower_user_id, followed_user_id):
        user_follow = UserFollow(follower_user_id=follower_user_id, followed_user_id=followed_user_id)
        db.session.add(user_follow)
        db.session.commit()

    @staticmethod
    def unfollow_user(follower_user_id, followed_user_id):
        user_follow = UserFollow.query.filter_by(follower_user_id=follower_user_id, followed_user_id=followed_user_id).first()
        if user_follow:
            db.session.delete(user_follow)
            db.session.commit()

    @staticmethod
    def get_following_count(user_id):
        return UserFollow.query.filter_by(follower_user_id=user_id).count()

    @staticmethod
    def get_follower_count(user_id):
        return UserFollow.query.filter_by(followed_user_id=user_id).count()
