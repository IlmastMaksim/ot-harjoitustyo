from database_connection import get_database_connection


class RecordRepository:
    def __init__(self, conn):
        self._conn = conn

    def save_workout_as_record(self, record):  # make a func to dump db
        cursor = self._conn.cursor()
        cursor.execute(
            "INSERT INTO records (exercise,sets,reps,created_on) VALUES (?,?,?,?);",
            (record.exercise, record.sets, record.reps, record.created_on),
        )
        self._conn.commit()
        return True

    def get_all_saved_records(self):
        cursor = self._conn.cursor()
        cursor.execute(
            "SELECT exercise, sets, reps, substr(created_on, 0, 11) as created_on FROM records;"
        )
        rows = cursor.fetchall()
        res = []
        for row in rows:
            res.append([row[0], row[1], row[2], row[3]])
        self._conn.commit()
        return res

    def get_all_exercises(self):
        cursor = self._conn.cursor()
        cursor.execute("SELECT exercise FROM records;")
        rows = cursor.fetchall()
        res = []
        for row in rows:
            res.append(row[0])
        self._conn.commit()
        return res

    def get_all_sets(self):
        cursor = self._conn.cursor()
        cursor.execute("SELECT sets FROM records;")
        rows = cursor.fetchall()
        res = []
        for row in rows:
            res.append(row[0])
        self._conn.commit()
        return res

    def get_all_reps(self):
        cursor = self._conn.cursor()
        cursor.execute("SELECT reps FROM records;")
        rows = cursor.fetchall()
        res = []
        for row in rows:
            res.append(row[0])
        self._conn.commit()
        return res

    def get_all_dates(self):
        cursor = self._conn.cursor()
        cursor.execute("SELECT substr(created_on, 0, 11) as created_on FROM records;")
        rows = cursor.fetchall()
        res = []
        for row in rows:
            res.append(row[0])
        self._conn.commit()
        return res


record_repository = RecordRepository(get_database_connection())
