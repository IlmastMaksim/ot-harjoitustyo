from database_connection import get_database_connection
from entities.user import User


class UserRepository:
    """

    Attributes:
        conn: yhteys tietokantaan
    """

    def __init__(self, conn):
        self._conn = conn

    def get_all_users(self):
        """Palauttaa kaikki tallennetut käyttäjät listan muodossa"""
        cursor = self._conn.cursor()
        cursor.execute(
            "SELECT username, email, password, substr(created_on, 0, 11) as created_on FROM users;"
        )
        rows = cursor.fetchall()
        res = []
        for row in rows:
            res.append([row[0], row[1], row[2], row[3]])
        self._conn.commit()
        return res

    def get_user_by_usename(self, username):
        cursor = self._conn.cursor()
        cursor.execute(
            "SELECT username, email, password, created_on FROM users WHERE username=?",
            (username,),
        )
        row = cursor.fetchone()
        return (
            User(row["username"], row["email"], row["password"], row["created_on"])
            if row
            else None
        )

    def get_user_by_email(self, email):
        cursor = self._conn.cursor()
        cursor.execute(
            "SELECT username, email, password, created_on FROM users WHERE email=?",
            (email,),
        )
        row = cursor.fetchone()
        return (
            User(row["username"], row["email"], row["password"], row["created_on"])
            if row
            else None
        )

    def add_new_user(self, user):
        cursor = self._conn.cursor()
        cursor.execute(
            "INSERT INTO users (username,email,password,created_on) VALUES (?,?,?,?);",
            (user.username, user.email, user.password, user.created_on),
        )
        self._conn.commit()
        return True

    def delete_data_about_users(self):
        cursor = self._conn.cursor()
        cursor.execute("DELETE FROM users;")
        self._conn.commit()
        return True

    def delete_user_by_username(self, username):
        cursor = self._conn.cursor()
        cursor.execute("DELETE FROM users WHERE username=?;", (username,))
        self._conn.commit()
        return True

    def delete_records_by_username(self, username):
        cursor = self._conn.cursor()
        cursor.execute("DELETE FROM records WHERE username=?;", (username,))
        self._conn.commit()
        return True


user_repository = UserRepository(get_database_connection())
