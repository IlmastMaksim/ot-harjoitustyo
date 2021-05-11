from database_connection import get_database_connection


class UserRepository:
    """

    Attributes:
        conn: yhteys tietokantaan
    """

    def __init__(self, conn):
        self._conn = conn

    def get_user_by_email(self, email):
        #sql = f"SELECT id, username, password FROM users WHERE email='{email}'"
        #cursor = self._conn.cursor()
        #cursor.execute(
        #    "SELECT id, username, password FROM users WHERE email=?"
        #)
        #self._conn.commit()
        #return user
        pass

    def add_new_user(self, username, email, password):
        sql = f"INSERT INTO users (username,email,password,created_on) VALUES ('{name}','{email}','{password}','{created_on}')"
        db.session.execute(sql)
        db.session.commit()
        return True


user_repository = UserRepository(get_database_connection())
