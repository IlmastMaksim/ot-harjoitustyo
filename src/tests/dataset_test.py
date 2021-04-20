import unittest
import requests
import random
from services.workout import (
    get_exercises_with_dumbbells,
    get_example_link_by_exercise,
    get_workout_data,
)


class DatasetTest(unittest.TestCase):
    def test_get_exercises_with_dumbbells(self):
        counter = 0
        exercises_with_dumbbells = get_exercises_with_dumbbells()
        for el in exercises_with_dumbbells:
            if "Dumbbells" not in el["Equipment"]:
                counter += 1
        self.assertEqual(counter, 0)

    def test_get_example_link_by_exercise(self):
        workout_data = get_workout_data()
        rand_dataobject = random.choice(workout_data)
        example_link = get_example_link_by_exercise(rand_dataobject["Exercise"])
        r = requests.head(example_link)
        self.assertEqual(r.status_code, 200)
