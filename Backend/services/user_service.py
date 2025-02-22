from repositories.user_repository import UserRepository
from models.user import User
from flask_bcrypt import generate_password_hash, check_password_hash

class UserService:
    @staticmethod
    def create_user(username, email, password):
        hashed_password = generate_password_hash(password).decode('utf-8')
        user = User(username=username, email=email, password=hashed_password, profileImage="", description="")
        UserRepository.add_user(user)
        return user

    @staticmethod
    def get_user_by_id(user_id):
        return UserRepository.get_user_by_id(user_id)

    @staticmethod
    def get_user_by_email(email):
        return UserRepository.get_user_by_email(email)

    @staticmethod
    def check_password(user, password):
        return check_password_hash(user.password, password)

    @staticmethod
    def update_user(user_id, user):
        updatedUser = UserRepository.get_user_by_id(user_id)
        if updatedUser:
            if 'username' in user:
                updatedUser.username = user['username']
            if 'profileImage' in user:
                updatedUser.profileImage = user['profileImage']
            if 'profileimage' in user:
                updatedUser.profileImage = user['profileimage']
            if 'description' in user:
                updatedUser.description = user['description']
            UserRepository.update_user(updatedUser)
            return updatedUser
        return None

    @staticmethod
    def filter_users_by_username(username):
        return UserRepository.filter_users_by_username(username)