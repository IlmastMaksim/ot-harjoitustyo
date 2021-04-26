from database_connection import get_database_connection


class RecordRepository:
    def __init__(self, conn):
        self._conn = conn

    def save_workout_as_record(self, record):
        cursor = self._conn.cursor()
        cursor.execute(
            "INSERT INTO records (exercise,sets,reps,created_on) VALUES (?,?,?,?);",
            (record.exercise, record.sets, record.reps, record.created_on),
        )
        self._conn.commit()
        return True

    def get_all_saved_records(self):
        cursor = self._conn.cursor()
        cursor.execute("SELECT * FROM records;")
        res = cursor.fetchall()
        self._conn.commit()
        return res


record_repository = RecordRepository(get_database_connection())
