import unittest
import string
import random
from services.record import record_services
from services.user import user_services


class DatabaseTest(unittest.TestCase):
    def setUp(self) -> None:
        self.test_id = 1
        self.test_username = "".join(
            random.choice(string.ascii_lowercase) for _ in range(10)
        )
        self.test_email = "".join(
            random.choice(string.ascii_lowercase) for _ in range(10)
        )
        self.test_password = "".join(
            random.choice(string.ascii_lowercase) for _ in range(10)
        )
        user_services.signup_user(
            self.test_username, self.test_email, self.test_password
        )

    def test_save_workout(self):
        dummy_dataset = {"Exercise": "Arnold Press", "Sets": 12, "Reps": 5}
        result = record_services.save_workout(
            dummy_dataset["Exercise"],
            dummy_dataset["Sets"],
            dummy_dataset["Reps"],
            self.test_id,
        )
        self.assertEqual(result, True)

    def test_get_all_records(self):
        records = record_services.get_all_records()
        self.assertGreater(len(records), 0)

    def test_get_all_saved_records_for_user(self):
        records = record_services.get_all_records_by_user(self.test_id)
        self.assertEqual(type(records), type([]))

    def test_count_times_exercises_done(self):
        exercises, times_exercises_done = record_services.count_times_exercises_done()
        self.assertEqual(type(exercises), type([]))
        self.assertEqual(type(times_exercises_done), type([]))
        self.assertGreater(len(exercises), 0)
        self.assertGreater(len(times_exercises_done), 0)

    def test_count_times_exercises_done_by_user(self):
        (
            exercises,
            times_exercises_done,
        ) = record_services.count_times_exercises_done_by_user(self.test_username)
        self.assertEqual(type(exercises), type([]))
        self.assertEqual(type(times_exercises_done), type([]))

    def test_count_workouts_per_day(self):
        records = record_services.count_workouts_per_day()
        self.assertGreater(len(records), 0)

    def test_count_workouts_per_day_by_user(self):
        records = record_services.count_workouts_per_day_by_user(self.test_username)
        self.assertEqual(type(records), type([]))
