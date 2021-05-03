from entities.record import Record
from repositories.record_repository import record_repository
from datetime import datetime
from dearpygui import core, simple


def get_timestamp():
    timestamp = datetime.now()
    created_on = timestamp.isoformat()
    return created_on


class RecordServices:
    def __init__(self):
        self._record_repo = record_repository

    def save_record(self, exercise, sets, reps):
        created_on = get_timestamp()
        result = self._record_repo.save_workout_as_record(
            Record(exercise, sets, reps, created_on)
        )
        return result

    def get_all_records(self):
        records = self._record_repo.get_all_saved_records()
        return records

    def get_all_exercises(self):
        exercises = self._record_repo.get_all_exercises()
        return exercises

    def get_all_sets(self):
        sets = self._record_repo.get_all_sets()
        return sets

    def get_all_reps(self):
        reps = self._record_repo.get_all_reps()
        return reps

    def get_all_dates(self):
        dates = self._record_repo.get_all_dates()
        return dates

    def count_times_exercises_done(self):
        exercises = self.get_all_exercises()
        counter = {}
        for exercise in exercises:
            if exercise not in counter:
                counter[exercise] = 0
            counter[exercise] += 1
        return list(counter.keys()), list(counter.values())

    def count_workouts_per_day(self):
        dates = self.get_all_dates()
        dates_dict = {}
        for date in dates:
            if date not in dates_dict:
                dates_dict[date] = 0
            dates_dict[date] += 1
        return list(dates_dict.values())


record_services = RecordServices()
