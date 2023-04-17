from db_connection import get_database_connection

def drop_tables(connection):
    cursor = connection.cursor()

    cursor.execute("DROP TABLE IF EXISTS Leaderboard;")

    connection.commit()


def create_tables(connection):

    cursor = connection.cursor()

    cursor.execute("CREATE TABLE Leaderboard (id integer PRIMARY KEY, name TEXT, time REAL);")

    connection.commit()


def initialize_database():
    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)


if __name__ == "__main__":
    initialize_database()