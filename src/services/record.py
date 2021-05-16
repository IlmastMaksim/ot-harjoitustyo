from entities.record import Record
from repositories.record_repository import record_repository
from util.util import get_timestamp


class RecordServices:
    """Luokka, jonka avulla toteutetaan sovelluslogikkaa liittyen käyttäjän tekimiin suorituksiin"""

    def __init__(self):
        self._record_repo = record_repository

    def save_workout(self, exercise, sets, reps, username):
        """Tallentaa suoritetun harjoituksen suorituksena

        Attributes:
            exercise: Kuvaa suoritetun harjoituksen nimettä
            sets: Kuvaa sarjojen määrää
            reps: Kuvaa toistojen määrää
            reps: Kuvaa käyttäjätunnusta
        """
        created_on = get_timestamp()
        result = self._record_repo.save_workout_as_record(
            Record(exercise, sets, reps, username, created_on)
        )
        return result

    def count_times_exercises_done(self):
        """Laskee kuinka paljon kertaa joka harjoitus oli suoritettu"""
        exercises = self._record_repo.get_all_exercises()
        counter = {}
        for exercise in exercises:
            if exercise not in counter:
                counter[exercise] = 0
            counter[exercise] += 1
        return list(counter.keys()), list(counter.values())

    def count_times_exercises_done_by_user(self, username):
        """Laskee kuinka paljon kertaa joka harjoitus oli suoritettu"""
        exercises = self._record_repo.get_all_exercises_by_username(username)
        counter = {}
        for exercise in exercises:
            if exercise not in counter:
                counter[exercise] = 0
            counter[exercise] += 1
        return list(counter.keys()), list(counter.values())

    def count_workouts_per_day(self):
        """Laskee paljonko harjoituksia suoritetaan päivittäin"""
        dates = self._record_repo.get_all_dates()
        dates_dict = {}
        for date in dates:
            if date not in dates_dict:
                dates_dict[date] = 0
            dates_dict[date] += 1
        return list(dates_dict.values())

    def count_workouts_per_day_by_user(self, username):
        """Laskee paljonko harjoituksia suoritetaan päivittäin"""
        dates = self._record_repo.get_all_dates_by_user(username)
        dates_dict = {}
        for date in dates:
            if date not in dates_dict:
                dates_dict[date] = 0
            dates_dict[date] += 1
        return list(dates_dict.values())

    def get_all_records(self):
        """Palauttaa kaikki tallennetut suoritukset listan muodossa"""
        records = self._record_repo.get_all_saved_records()
        return records

    def get_all_records_by_user(self, username):
        """Palauttaa kaikki tallennetut suoritukset listan muodossa"""
        records_for_user = self._record_repo.get_all_saved_records_by_user(username)
        return records_for_user


record_services = RecordServices()
