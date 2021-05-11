import unittest
from services.record import record_services


class DatabaseTest(unittest.TestCase):
    def test_data_is_saved(self):
        dummy_dataset = {"Exercise": "Arnold Press", "Sets": 12, "Reps": 5}
        result = record_services.save_workout(dummy_dataset["Exercise"], dummy_dataset["Sets"], dummy_dataset["Reps"])
        self.assertEqual(result, True)

    def test_data_can_be_fetched(self):
        records = record_services.get_all_records()
        self.assertGreater(len(records), 0)

    def test_count_workouts_per_day(self):
        records = record_services.count_workouts_per_day()
        self.assertGreater(len(records), 0)

    def test_count_times_exercises_done(self):
        exercises, times_exercises_done = record_services.count_times_exercises_done()
        self.assertEqual(type(exercises), type([]))
        self.assertEqual(type(times_exercises_done), type([]))
        self.assertGreater(len(exercises), 0)
        self.assertGreater(len(times_exercises_done), 0)

    def test_get_all_exercises(self):
        all_exercises = record_services.get_all_exercises()
        self.assertGreater(len(all_exercises), 0)

    def test_get_all_dates(self):
        all_dates = record_services.get_all_dates()
        self.assertGreater(len(all_dates), 0)
