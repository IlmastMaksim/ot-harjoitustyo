from database_connection import get_database_connection


class RecordRepository:
    """Luokka, jonka avulla vuorovaikutetaan "records"-tietokannan kanssa

    Attributes:
        conn: yhteys tietokantaan
    """

    def __init__(self, conn):
        self._conn = conn

    def save_workout_as_record(self, workout):
        """Tallentaa suoritetun harjoituksen suorituksena

        Attributes:
            workout: suoritettu harjoitus
        """
        cursor = self._conn.cursor()
        cursor.execute(
            "INSERT INTO records (exercise,sets,reps,username,created_on) VALUES (?,?,?,?,?);",
            (
                workout.exercise,
                workout.sets,
                workout.reps,
                workout.username,
                workout.created_on,
            ),
        )
        self._conn.commit()
        return True

    def get_all_saved_records(self):
        """Palauttaa kaikki tallennetut suoritukset listan muodossa"""
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

    def get_all_saved_records_for_user(self, username):
        """Palauttaa kaikki tallennetut suoritukset listan muodossa"""
        cursor = self._conn.cursor()
        cursor.execute(
            "SELECT exercise, sets, reps, substr(created_on, 0, 11) as created_on FROM records WHERE username=?;",
            (username,),
        )
        rows = cursor.fetchall()
        res = []
        for row in rows:
            res.append([row[0], row[1], row[2], row[3]])
        self._conn.commit()
        return res

    def get_all_exercises(self):
        """Palauttaa kaiken tallentujen harjoitusten nimet listan muodossa"""
        cursor = self._conn.cursor()
        cursor.execute("SELECT exercise FROM records;")
        rows = cursor.fetchall()
        res = []
        for row in rows:
            res.append(row[0])
        self._conn.commit()
        return res

    def get_all_exercises_by_username(self, username):
        """Palauttaa kaiken tallentujen harjoitusten nimet listan muodossa"""
        cursor = self._conn.cursor()
        cursor.execute("SELECT exercise FROM records WHERE username=?;", (username,))
        rows = cursor.fetchall()
        res = []
        for row in rows:
            res.append(row[0])
        self._conn.commit()
        return res

    def get_all_dates(self):
        """Palauttaa kaiken tallentujen harjoitusten määräaikat listan muodossa"""
        cursor = self._conn.cursor()
        cursor.execute("SELECT substr(created_on, 0, 11) as created_on FROM records;")
        rows = cursor.fetchall()
        res = []
        for row in rows:
            res.append(row[0])
        self._conn.commit()
        return res

    def get_all_dates_by_user(self, username):
        """Palauttaa kaiken tallentujen harjoitusten määräaikat listan muodossa"""
        cursor = self._conn.cursor()
        cursor.execute(
            "SELECT substr(created_on, 0, 11) as created_on FROM records WHERE username=?;",
            (username,),
        )
        rows = cursor.fetchall()
        res = []
        for row in rows:
            res.append(row[0])
        self._conn.commit()
        return res


record_repository = RecordRepository(get_database_connection())
