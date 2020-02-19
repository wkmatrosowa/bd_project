from mysql_adapter import mysql_adapter
from sql_tables.sql_table import SQLTable


class BandTable(SQLTable):

    __name = 'band'
    __INSERT_SQL = "INSERT INTO band (bandname, yearoffoundation) VALUES (%s, %s)"
    __UPDATE_SQL = ""
    __DELETE_SQL = ""
    __SELECT_SQL = "SELECT * FROM band"
    allowable_keys = ['id', 'bandname', 'yearoffoundation']

    def __init__(self):
        pass

    def insert(self, bandname: str = "", yearoffoundation: str = ""):
        mysql_adapter.execute_with_params(query=self.__INSERT_SQL, params=(bandname, yearoffoundation))

    def update(self):
        pass

    def delete(self):
        pass

    def find(self, request: dict):
        return mysql_adapter.select(self.__SELECT_SQL + self.generate_where(request.keys()), tuple(request.values()))
