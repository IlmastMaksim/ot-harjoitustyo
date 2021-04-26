from database_connection import get_database_connection


def drop_tables(connection):
    cursor = connection.cursor()

    cursor.execute(
        """
        drop table if exists records;
    """
    )

    connection.commit()


def create_tables(connection):
    cursor = connection.cursor()

    cursor.execute(
        """
        create table records (
            id INTEGER PRIMARY KEY,
            exercise TEXT,
            sets INTEGER,
            reps INTGER,
            created_on TEXT
        );
    """
    )

    connection.commit()


def initialize_database():
    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)
