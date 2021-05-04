import unittest
import requests
import random
from services.workout import workout_services, get_workout_data


class DatasetTest(unittest.TestCase):
    def test_get_exercises_with_dumbbells(self):
        counter = 0
        exercises_with_dumbbells = workout_services.get_exercises_with_dumbbells()
        for el in exercises_with_dumbbells:
            if "Dumbbells" not in el["Equipment"]:
                counter += 1
        self.assertEqual(counter, 0)

    def test_get_example_link_by_exercise(self):
        workout_data = get_workout_data()
        rand_dataobject = random.choice(workout_data)
        example_link = workout_services.get_example_link_by_exercise(
            rand_dataobject["Exercise"]
        )
        r = requests.head(example_link)
        self.assertEqual(r.status_code, 200)

    def test_get_criterias_by_name(self):
        test_name = "Exercise Type"
        dummy_res = ["Weight", "Machine", "Cardio", "Laps", "Plyo"]
        workout_data = get_workout_data()
        criterias_by_name = workout_services.get_criterias_by_name(test_name)
        self.assertEqual(len(dummy_res), len(criterias_by_name))
        dummy_res.sort()
        criterias_by_name.sort()
        arrays_not_equal = True
        for i in range(len(criterias_by_name)):
            if dummy_res[i] != criterias_by_name[i]:
                arrays_not_equal = False
        self.assertEqual(arrays_not_equal, True)

    def test_get_composed_workout(self):
        dummy_set = ["Dumbbells", "Weight", "Arms"]
        composed_workout = workout_services.get_composed_workout(
            dummy_set[0], dummy_set[1], dummy_set[2]
        )
        self.assertEqual(len(composed_workout), 5)
