from repositories.user_follow_repository import UserFollowRepository
from repositories.user_repository import UserRepository

class UserFollowService:
    @staticmethod
    def follow_user(follower_user_id, followed_user_id):
        if not UserRepository.get_user_by_id(follower_user_id):
            raise ValueError("Follower user ID does not exist")
        if not UserRepository.get_user_by_id(followed_user_id):
            raise ValueError("Followed user ID does not exist")
        UserFollowRepository.follow_user(follower_user_id, followed_user_id)

    @staticmethod
    def unfollow_user(follower_user_id, followed_user_id):
        if not UserRepository.get_user_by_id(follower_user_id):
            raise ValueError("Follower user ID does not exist")
        if not UserRepository.get_user_by_id(followed_user_id):
            raise ValueError("Followed user ID does not exist")
        UserFollowRepository.unfollow_user(follower_user_id, followed_user_id)

    @staticmethod
    def get_following_count(user_id):
        if not UserRepository.get_user_by_id(user_id):
            raise ValueError("User ID does not exist")
        return UserFollowRepository.get_following_count(user_id)

    @staticmethod
    def get_follower_count(user_id):
        if not UserRepository.get_user_by_id(user_id):
            raise ValueError("User ID does not exist")
        return UserFollowRepository.get_follower_count(user_id)
