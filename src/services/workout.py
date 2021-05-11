from random import sample
from re import findall
from util.util import get_workout_data


class WorkoutServices:
    """Luokka, jonka avulla toteutetaan sovelluslogikkaa, joka säveltää harjotuksen annetuin parametrien pohjalla"""

    def __init__(self):
        self.data = get_workout_data()

    def get_exercises_with_dumbbells(self):
        """Palauttaa kaikki harjoitukset, jotka suoritetaan käyttäen käsipainoja"""
        exercises_with_dumbbells = []
        for data_obj in self.data:
            if "Dumbbells" in data_obj["Equipment"]:
                exercises_with_dumbbells.append(data_obj)
        return exercises_with_dumbbells

    def get_criterias_by_name(self, name):
        """Palauttaa harjoitusten kriteriat listan muodossa mm. "equipment" -> "Bar,Dumbbells,Cable..."

        Attributes:
            nimi: kriterian nimi
        """
        criterias = []
        for data_obj in self.data:
            categories = data_obj[name].split(",")
            for category in categories:
                if category not in criterias:
                    criterias.append(category)
        return criterias

    def get_composed_workout(self, equipment, exercise_type, muscle_group):
        """Säveltää harjoituksen kriterein pohjalla

        Attributes:
            equipment: harjoituksessa käyttävät varusteet
            exercise_type: harjoituksen tyypi
            muscle_group: lihasryhmät, joihin keskeytetään
        """
        workout = []
        for data_obj in self.data:
            if (
                (
                    equipment in data_obj["Equipment"]
                    and exercise_type in data_obj["Exercise Type"]
                )
                or (
                    equipment in data_obj["Equipment"]
                    and muscle_group in data_obj["Major Muscle"]
                )
                or (
                    exercise_type in data_obj["Exercise Type"]
                    and muscle_group in data_obj["Major Muscle"]
                )
            ):
                workout.append(
                    {
                        "Exercise": data_obj["Exercise"],
                        "Sets": "0",
                        "Reps": "0",
                        "Example": "Show Example",
                    }
                )
        return sample(workout, 5) if len(workout) > 5 else workout

    def get_example_link_by_exercise(self, exercise):
        """Palauttaa gif-kuvan sisältävän linkin, jonka avulla voi tallentaa sen kuvan

        Attributes:
            exercise: harjoituksen nimi
        """
        for data_obj in self.data:
            if data_obj["Exercise"] == exercise:
                return findall(r"\(.*?\)", data_obj["Example"])[0][1:-1]


workout_services = WorkoutServices()
