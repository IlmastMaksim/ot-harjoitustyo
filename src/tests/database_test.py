import unittest
from services.record import record_services


class DatabaseTest(unittest.TestCase):
    # def test_data_is_saved(self):
    #    dummy_dataset = {"Exercise": "Arnold Press", "Sets": 12, "Reps": 5}
    #    result = record_services.save_record(
    #        dummy_dataset["Exercise"], dummy_dataset["Sets"], dummy_dataset["Reps"]
    #    )
    #    records = record_services.get_all_records()
    #    self.assertEqual(result, True)

    def test_data_can_be_fetched(self):
        records = record_services.get_all_records()
        self.assertGreater(len(records), 0)

    def test_count_workouts_per_day(self):
        records = record_services.count_workouts_per_day()
        self.assertGreater(len(records), 0)