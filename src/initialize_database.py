from database_connection import get_database_connection


def drop_tables(connection):
    cursor = connection.cursor()

    cursor.execute(
        """
            DROP TABLE IF EXISTS records;
        """
    )

    cursor.execute(
        """
            DROP TABLE IF EXISTS users;
        """
    )

    connection.commit()


def create_tables(connection):
    cursor = connection.cursor()

    cursor.execute(
        """
            CREATE TABLE records (
                id INTEGER PRIMARY KEY,
                exercise TEXT,
                sets INTEGER,
                reps INTGER,
                username INTEGER REFERENCES users ON DELETE CASCADE,
                created_on TEXT
            );
        """
    )

    cursor.execute(
        """
            CREATE TABLE users (
                id INTEGER PRIMARY KEY,
                username TEXT UNIQUE NOT NULL,
                email TEXT UNIQUE NOT NULL,
                password TEXT,
                created_on TEXT
            );
        """
    )

    connection.commit()


def initialize_database():
    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)
