from db_connection import get_database_connection


class Leaderboard:
    def __init__(self):
        """Class for handling sql commands

        Attributes:
            _connection: database connection
            _cursor: connection cursor to run commands
        """
        self._connection = get_database_connection()
        self._cursor = self._connection.cursor()

    def _get_grid_table(self, grid_size: tuple):
        return f"_{grid_size[0]}x{grid_size[1]}"

    def insert_time(self, grid_size: tuple, name: str, time: str):
        """Inserts name finish time into the correct leaderboard

        Args:
            grid_size (tuple): the played game's grid size
            name (str): name that was selected in menu
            time (str): finish time as a two decimal float value
        """
        table = self._get_grid_table(grid_size)
        self._cursor.execute(
            f"INSERT INTO {table} (name, time) VALUES (?, ?)",
            (name, time)
        )
        self._connection.commit()

    def grid_leaderboard(self, grid_size: tuple):
        """Gives the names and times of the 10 fastest runs for the selected grid size

        Args:
            grid_size (tuple): the played game's grid size

        Returns:
            list: list of tuples containing the names and times of the runs
        """
        table = self._get_grid_table(grid_size)
        result = self._cursor.execute(
            f"SELECT name, time FROM {table} ORDER BY time LIMIT 10").fetchall()
        return result

    def delete_all(self):
        """Clears all tables. This is used for testing
        """
        self._cursor.execute("DELETE FROM _8x8")
        self._cursor.execute("DELETE FROM _16x16")
        self._cursor.execute("DELETE FROM _24x16")
        self._connection.commit()

    def get_all(self, grid_size: tuple):
        """Selects everything from every table one at a time. This is used for testing

        Args:
            grid_size (tuple): the test loop's given grid size

        Returns:
            list: list of tuples containing all information in the row
        """
        table = self._get_grid_table(grid_size)
        result = self._cursor.execute(
            f"SELECT * FROM {table}").fetchall()
        return result

    def get_tables(self):
        """Returns the names of all tables in the database file.
           This is used to ensure that the program cannot be run before running the command build.

        Returns:
            list: list of tuples containing the table names
        """
        query = "SELECT name FROM sqlite_master WHERE type='table'"
        result = self._cursor.execute(query).fetchall()
        return result
