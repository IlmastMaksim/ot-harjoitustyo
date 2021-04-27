from entities.record import Record
from repositories.record_repository import record_repository
from datetime import datetime


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


record_services = RecordServices()
