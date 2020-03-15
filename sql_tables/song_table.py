from mysql_adapter import mysql_adapter
from sql_tables.sql_table import SQLTable


class SongTable(SQLTable):
    __name = 'song'
    __INSERT_SQL = "INSERT INTO song (songname, id_album) VALUES (%s, %s)"
    __UPDATE_SQL = "UPDATE song SET songname = %s WHERE id = %s"
    __DELETE_SQL = "DELETE FROM song WHERE id = %s"
    __SELECT_SQL = "SELECT * FROM song"
    allowable_keys = ['id', 'songname', 'id_album']

    def __init__(self):
        pass

    def insert(self, songname: str = "", id_album: str = ""):
        mysql_adapter.execute_with_params(query=self.__INSERT_SQL, params=(songname, id_album))

    def update(self, songname: str = "", id: str = ""):
        mysql_adapter.execute_with_params(query=self.__UPDATE_SQL, params=(songname, id))

    def delete(self, id: str):
        mysql_adapter.execute_with_params(query=self.__DELETE_SQL, params=(id,))

    def find(self, request: dict):
        return mysql_adapter.select(self.__SELECT_SQL + self.generate_where(request.keys()), tuple(request.values()))
