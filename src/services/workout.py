import json
from random import sample
from re import findall


def get_workout_data():
    with open("./src/data/dataset.json", "r") as read_file:
        data = json.load(read_file)
        return data


def get_exercises_with_dumbbells():
    data = get_workout_data()
    exercises_with_dumbbells = []
    for el in data:
        if "Dumbbells" in el["Equipment"]:
            exercises_with_dumbbells.append(el)
    return exercises_with_dumbbells


def get_criterias_by_name(name):
    data = get_workout_data()
    criterias = []
    for el in data:
        categories = el[name].split(",")
        for category in categories:
            if category not in criterias:
                criterias.append(category)
    return criterias


def get_composed_workout(equipment, exercise_type, muscle_group):
    data = get_workout_data()
    workout = []
    for el in data:
        if (
            (equipment in el["Equipment"] and exercise_type in el["Exercise Type"])
            or (equipment in el["Equipment"] and muscle_group in el["Major Muscle"])
            or (
                exercise_type in el["Exercise Type"]
                and muscle_group in el["Major Muscle"]
            )
        ):
            workout.append(
                {
                    "Exercise": el["Exercise"],
                    "Sets": "0",
                    "Reps": "0",
                    "Example": "Show Example",
                }
            )
    return sample(workout, 5) if len(workout) > 5 else workout


def get_example_link_by_exercise(exercise):
    data = get_workout_data()
    for el in data:
        if el["Exercise"] == exercise:
            return findall(r"\(.*?\)", el["Example"])[0][1:-1]
