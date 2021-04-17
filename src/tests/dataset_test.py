import unittest
from services.workout import get_exercises_with_dumbbells

class DatasetTest(unittest.TestCase):
    def test_get_exercises_with_dumbbells(self):
        counter = 0
        exercises_with_dumbbells = get_exercises_with_dumbbells()
        for el in exercises_with_dumbbells:
            if "Dumbbells" not in el["Equipment"]:
                counter += 1
        self.assertEqual(counter, 0)



