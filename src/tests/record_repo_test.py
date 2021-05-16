import unittest
from entities.record import Record
from repositories.record_repository import record_repository
from util.util import get_timestamp


class RecordServiceTest(unittest.TestCase):
    def setUp(self):
        self.user_id = 1
        self.exercise_name = "Arnold Press"
        self.username = "test"
        created_on = get_timestamp()
        record_repository.save_workout_as_record(
            Record(self.exercise_name, 12, 3, self.username, created_on)
        )

    def test_save_workout_as_record(self):
        created_on = get_timestamp()
        result = record_repository.save_workout_as_record(
            Record("test", 12, 3, "test123", created_on)
        )
        self.assertEqual(result, True)

    def test_get_all_saved_records(self):
        records = record_repository.get_all_saved_records()
        self.assertEqual(type([]), type(records))

    def test_get_all_saved_records_by_user(self):
        records = record_repository.get_all_saved_records_by_user(self.username)
        self.assertEqual(type([]), type(records))

    def test_get_all_exercises(self):
        exercises = record_repository.get_all_exercises()
        self.assertEqual(type([]), type(exercises))

    def test_get_all_exercises_by_username(self):
        exercises = record_repository.get_all_exercises_by_username(self.username)
        self.assertEqual(type([]), type(exercises))

    def test_get_all_dates(self):
        dates = record_repository.get_all_dates()
        self.assertEqual(type([]), type(dates))

    def test_get_all_dates_by_user(self):
        dates = record_repository.get_all_dates_by_user(self.username)
        self.assertEqual(type([]), type(dates))
