from db_connection import get_database_connection


def drop_tables(connection):
    cursor = connection.cursor()

    cursor.execute("DROP TABLE IF EXISTS _8x8;")
    cursor.execute("DROP TABLE IF EXISTS _16x16;")
    cursor.execute("DROP TABLE IF EXISTS _24x16;")

    connection.commit()


def create_tables(connection):

    cursor = connection.cursor()

    cursor.execute(
        "CREATE TABLE _8x8 (id integer PRIMARY KEY, name TEXT, time FLOAT);")
    cursor.execute(
        "CREATE TABLE _16x16 (id integer PRIMARY KEY, name TEXT, time FLOAT);")
    cursor.execute(
        "CREATE TABLE _24x16 (id integer PRIMARY KEY, name TEXT, time FLOAT);")

    connection.commit()


def initialize_database():
    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)


if __name__ == "__main__":
    initialize_database()
