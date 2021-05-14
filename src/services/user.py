from entities.user import User
from repositories.user_repository import user_repository
from util.util import encrypt_password, verify_password, get_timestamp


class UserServices:
    """Luokka"""

    def __init__(self):
        self._user_repo = user_repository
        self._user = None

    def get_all_users(self):
        return self._user_repo.get_all_users()

    def login_user(self, username, password):
        user = self._user_repo.get_user_by_usename(username)
        if not user:
            return False
        was_password_verified = verify_password(password, user.password)
        if was_password_verified:
            self._user = user
            return True
        return False

    def signup_user(self, username, email, password):
        user_by_username = self._user_repo.get_user_by_usename(username)
        user_by_email = self._user_repo.get_user_by_email(email)
        if user_by_email or user_by_username:
            return False
        hash_value = encrypt_password(password)
        created_on = get_timestamp()
        result = self._user_repo.add_new_user(
            User(username, email, hash_value, created_on)
        )
        return result

    def get_current_user(self):
        return self._user


user_services = UserServices()
