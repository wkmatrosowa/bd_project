from mysql_adapter import mysql_adapter
from sql_tables.sql_table import SQLTable


class BandTable(SQLTable):

    __name = 'band'
    __INSERT_SQL = "INSERT INTO band (bandname, yearoffoundation) VALUES (%s, %s)"
    __UPDATE_SQL = "UPDATE band SET bandname = %s, yearoffoundation = %s WHERE id = %s"
    __DELETE_SQL = ""
    __SELECT_SQL = "SELECT * FROM band"
    __PARTICIPANTS_SQL = """
    SELECT * FROM musician RIGHT JOIN participants ON musician.id = participants.id_musician 
    WHERE participants.id_band = %s
    """
    __CANDIDATES_SQL = ""
    allowable_keys = ['id', 'bandname', 'yearoffoundation', 'id_musician', 'firstname', 'surname', 'specialization']

    def __init__(self):
        pass

    def insert(self, bandname: str = "", yearoffoundation: str = ""):
        mysql_adapter.execute_with_params(query=self.__INSERT_SQL, params=(bandname, yearoffoundation))

    def update(self, bandname: str, yearoffoundation: str, id: str):
        mysql_adapter.execute_with_params(query=self.__UPDATE_SQL, params=(bandname, yearoffoundation, id))

    def delete(self):
        pass

    def find(self, request: dict):
        return mysql_adapter.select(self.__SELECT_SQL + self.generate_where(request.keys()), tuple(request.values()))

    def get_participants(self, id: str):
        return mysql_adapter.select(self.__PARTICIPANTS_SQL, (id, ))
