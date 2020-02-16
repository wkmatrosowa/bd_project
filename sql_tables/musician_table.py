from mysql_helper import mysql_helper
from sql_tables.sql_table import SQLTable


class MusicianTable(SQLTable):
    __name = 'musician'
    __INSERT_SQL = "INSERT INTO musician (firstname, surname, specialization) VALUES (%s, %s, %s)"
    __UPDATE_SQL = "UPDATE musician SET firstname = %s, surname = %s, specialization = %s WHERE id = %s"
    __DELETE_SQL = "DELETE FROM musician WHERE id = %s"
    __SELECT_SQL = "SELECT * FROM musician"
    allowable_keys = ['id', 'firstname', 'surname', 'specialization']

    def __init__(self):
        pass

    def insert(self, firstname: str = "", surname: str = "", specialization: str = ""):
        mysql_helper.execute_with_params(query=self.__INSERT_SQL, params=(firstname, surname, specialization))

    def update(self, firstname: str, surname: str, specialization: str, id: str):
        mysql_helper.execute_with_params(query=self.__UPDATE_SQL, params=(firstname, surname, specialization, id))

    def delete(self, id: str):
        mysql_helper.execute_with_params(query=self.__DELETE_SQL, params=(id,))

    def find(self, request: dict):
        return mysql_helper.select(self.__SELECT_SQL + self.generate_where(request.keys()), tuple(request.values()))
