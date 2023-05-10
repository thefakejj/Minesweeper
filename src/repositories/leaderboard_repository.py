from db_connection import get_database_connection


class Leaderboard:
    def __init__(self):
        self._connection = get_database_connection()
        self._cursor = self._connection.cursor()

    def _get_grid_table(self, grid_size):
        return f"_{grid_size[0]}x{grid_size[1]}"

    def insert_time(self, grid_size, name, time):
        table = self._get_grid_table(grid_size)
        self._cursor.execute(
            f"INSERT INTO {table} (name, time) VALUES (?, ?)",
            (name, time)
        )
        self._connection.commit()

    def grid_leaderboard(self, grid_size):
        table = self._get_grid_table(grid_size)
        result = self._cursor.execute(
            f"SELECT name, time FROM {table} ORDER BY time LIMIT 10").fetchall()
        return result
