from entities.user import User
from repositories.user_repository import user_repository
from util.util import encrypt_password, verify_password, get_timestamp


class UserServices:
    """Luokka"""

    def __init__(self):
        self._user_repo = user_repository
        self._user = None

    def log_in(self):
        return True

    def login(self, email, password):
        user = self._user_repo.get_user_by_email(email)
        if user == None:
            return False
        else:
            if verify_password(password, user.password):
                return True
            else:
                return False

    def signup_user(self, username, email, password):
        hash_value = encrypt_password(password)
        created_on = get_timestamp()
        try:
            self._user_repo.add_new_user(username, email, password, created_on)
        except:
            return False
        return True

    def get_current_user(self):
        return self._user


user_services = UserServices()
