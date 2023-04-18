from db_connection import get_database_connection


def list_best_times_8x8_all_users(connection):
    cursor = connection.cursor()
    result = cursor.execute(
        "SELECT name, time FROM _8x8 ORDER BY time LIMIT 10;").fetchall()
    return result


def insert_jasper_record_breaking_pace(connection):
    cursor = connection.cursor()
    length_query = int(cursor.execute(
        "SELECT count(*) FROM _8x8;").fetchone()[0])
    if length_query < 1:
        cursor.execute(
            "INSERT INTO _8x8 (name, time) VALUES ('Jasper', '41.5437877');")

        connection.commit()
    return True


def run_tests():
    connection = get_database_connection()
    # insert_jasper_record_breaking_pace(connection)
    print(list_best_times_8x8_all_users(connection))


if __name__ == "__main__":
    run_tests()
