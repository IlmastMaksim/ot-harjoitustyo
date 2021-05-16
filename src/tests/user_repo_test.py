import unittest
import random
import string
from entities.user import User
from repositories.user_repository import user_repository
from util.util import get_timestamp


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
        created_on = get_timestamp()
        user_repository.add_new_user(
            User(self.test_username, self.test_email, self.test_password, created_on)
        )

    def test_get_all_users(self):
        users = user_repository.get_all_users()
        self.assertEqual(type([]), type(users))

    def test_get_user_by_usename(self):
        user = user_repository.get_user_by_usename(self.test_username)
        self.assertIsNotNone(user)
        self.assertIsNotNone(user.password)

    def test_get_user_by_email(self):
        user = user_repository.get_user_by_email(self.test_email)
        self.assertIsNotNone(user)
        self.assertIsNotNone(user.password)

    def test_add_new_user(self):
        test_user = {
            "username": "test11",
            "email": "test11@test.com",
            "password": "test",
        }
        created_on = get_timestamp()
        result = user_repository.add_new_user(
            User(
                test_user["username"],
                test_user["email"],
                test_user["password"],
                created_on,
            )
        )
        self.assertEqual(True, result)

    def test_delete_data_about_users(self):
        result = user_repository.delete_data_about_users()
        self.assertEqual(True, result)

    def test_delete_user_by_username(self):
        result = user_repository.delete_user_by_username(self.test_username)
        self.assertEqual(True, result)

    def test_delete_records_by_username(self):
        result = user_repository.delete_records_by_username(self.test_username)
        self.assertEqual(True, result)
