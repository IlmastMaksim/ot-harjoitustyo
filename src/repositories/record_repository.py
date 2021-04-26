from entities.record import Record
from database_connection import get_database_connection


class RecordRepository:
    def __init__(self, conn):
        self._conn = conn

    def save_workout_as_record():
        cursor = self.conn.cursor()
        cursor.execute(
            "insert into records (exercise,sets,reps,created_on) values (?,?,?,?)",
            (exercise, sets, reps, created_on),
        )
        self._conn.commit()
        return True


record_repository = RecordRepository(get_database_connection())
