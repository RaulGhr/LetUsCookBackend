from models.user_follow import UserFollow
from extensions import db

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

    @staticmethod
    def get_following_users(user_id):
        return UserFollow.query.filter_by(follower_user_id=user_id).all()

    @staticmethod
    def is_following(follower_user_id, followed_user_id):
        return UserFollow.query.filter_by(follower_user_id=follower_user_id, followed_user_id=followed_user_id).first() is not None

    @staticmethod
    def get_following_ids(user_id):
        following = UserFollow.query.filter_by(follower_user_id=user_id).with_entities(
            UserFollow.followed_user_id).all()
        return [user[0] for user in following]
