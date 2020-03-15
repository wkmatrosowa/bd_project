from mysql_adapter import mysql_adapter
from sql_tables.sql_table import SQLTable


class AlbumTable(SQLTable):
    __name = 'album'
    __INSERT_SQL = "INSERT INTO album (albumname, year, genre, id_performer) VALUES (%s, %s, %s, %s)"
    __UPDATE_SQL = "UPDATE album SET albumname = %s, year = %s, genre = %s WHERE id = %s"
    __DELETE_SQL = "DELETE FROM album WHERE id = %s"
    __SELECT_SQL = "SELECT * FROM album"
    allowable_keys = ['id', 'albumname', 'year', 'genre', 'id_performer']

    def __init__(self):
        pass

    def insert(self, albumname: str = "", year: str = "", genre: str = "", id_performer: str = ""):
        mysql_adapter.execute_with_params(query=self.__INSERT_SQL, params=(albumname, year, genre, id_performer))

    def update(self, albumname: str = "", year: str = "", genre: str = "", id: str = ""):
        mysql_adapter.execute_with_params(query=self.__UPDATE_SQL, params=(albumname, year, genre, id))

    def delete(self, id: str):
        mysql_adapter.execute_with_params(query=self.__DELETE_SQL, params=(id,))

    def find(self, request: dict):
        return mysql_adapter.select(self.__SELECT_SQL + self.generate_where(request.keys()), tuple(request.values()))
