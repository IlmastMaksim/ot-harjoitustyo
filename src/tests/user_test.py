import unittest
from services.user import user_services


class DatabaseTest(unittest.TestCase):
    def test_signup_user(self):
        test_user = {"username": "test", "email": "test1@test.com", "password": "123"}
        result = user_services.signup_user(
            test_user["username"], test_user["email"], test_user["password"]
        )
        self.assertEqual(result, True)

    def test_login_user(self):
        test_user = {"username": "test", "email": "test1@test.com", "password": "123"}
        user_services.signup_user(
            test_user["username"], test_user["email"], test_user["password"]
        )
        result = user_services.login_user(test_user["username"], test_user["password"])
        self.assertEqual(result, True)
        username = user_services.get_current_user().username
        self.assertEqual(username, test_user["username"])
