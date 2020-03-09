from mysql_adapter import mysql_adapter
from sql_tables.sql_table import SQLTable


class BandTable(SQLTable):
    __name = 'band'
    __INSERT_SQL = "INSERT INTO band (bandname, yearoffoundation) VALUES (%s, %s)"
    __UPDATE_SQL = "UPDATE band SET bandname = %s, yearoffoundation = %s WHERE id = %s"
    __DELETE_SQL = "DELETE FROM band WHERE id = %s"
    __SELECT_SQL = "SELECT * FROM band"
    __PARTICIPANTS_SQL = """
    SELECT * FROM musician RIGHT JOIN participants ON musician.id = participants.id_musician 
    WHERE participants.id_band = %s
    """
    __CANDIDATES_SQL = """
    SELECT * FROM musician LEFT JOIN participants ON musician.id = participants.id_musician
    WHERE NOT EXISTS (select 1 from participants where participants.id_band = %s AND participants.id_musician=musician.id)
    """
    __ADD_CANDIDATES = """
        INSERT INTO participants(id_musician, id_band) VALUES (%s, %s)
    """
    allowable_keys = ['id', 'bandname', 'yearoffoundation', 'id_musician', 'firstname', 'surname', 'specialization']

    def __init__(self):
        pass

    def insert(self, bandname: str = "", yearoffoundation: str = ""):
        mysql_adapter.execute_with_params(query=self.__INSERT_SQL, params=(bandname, yearoffoundation))

    def update(self, bandname: str, yearoffoundation: str, id: str):
        mysql_adapter.execute_with_params(query=self.__UPDATE_SQL, params=(bandname, yearoffoundation, id))

    def delete(self, id: str):
        mysql_adapter.execute_with_params(query=self.__DELETE_SQL, params=(id,))

    def find(self, request: dict):
        return mysql_adapter.select(self.__SELECT_SQL + self.generate_where(request.keys()), tuple(request.values()))

    def get_participants(self, id: str):
        return mysql_adapter.select(self.__PARTICIPANTS_SQL, (id,))

    def get_candidates(self, id: str):
        return mysql_adapter.select(self.__CANDIDATES_SQL, (id,))

    def add_candidate(self, id_band, id_musician):
        mysql_adapter.execute_with_params(self.__ADD_CANDIDATES, (id_musician, id_band))
