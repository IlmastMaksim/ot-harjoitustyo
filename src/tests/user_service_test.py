import unittest
import string
import random
from services.user import user_services


class UserServiceTest(unittest.TestCase):
    def setUp(self):
        self.test_username = "".join(
            random.choice(string.ascii_lowercase) for _ in range(10)
        )
        self.test_email = "".join(
            random.choice(string.ascii_lowercase) for _ in range(10)
        )
        self.test_password = "".join(
            random.choice(string.ascii_lowercase) for _ in range(10)
        )

    def test_signup_user(self):
        result = user_services.signup_user(
            self.test_username, self.test_email, self.test_password
        )
        self.assertEqual(result, True)

    def test_login_user(self):
        user_services.signup_user(
            self.test_username, self.test_email, self.test_password
        )
        result = user_services.login_user(self.test_username, self.test_password)
        self.assertEqual(result, True)
        username = user_services.get_current_user().username
        self.assertEqual(username, self.test_username)

    def test_delete_data_about_users(self):
        user_services.signup_user(
            self.test_username, self.test_email, self.test_password
        )
        result = user_services.delete_data_about_users()
        self.assertEqual(True, result)

    def test_delete_user_by_username(self):
        user_services.signup_user(
            self.test_username, self.test_email, self.test_password
        )
        result = user_services.delete_user_by_username(self.test_username)
        self.assertEqual(True, result)

    def test_delete_user_by_username(self):
        user_services.signup_user(
            self.test_username, self.test_email, self.test_password
        )
        user_services.login_user(self.test_username, self.test_password)
        result = user_services.delete_user_by_username(self.test_username)
        self.assertEqual(True, result)
