from mysql_adapter import mysql_adapter
from sql_tables.sql_table import SQLTable


class PerformerTable(SQLTable):
    __INSERT_IF_BAND_SQL = "INSERT INTO performer (id_band) VALUES(%s)"
    __INSERT_IF_MUSICIAN_SQL = "INSERT INTO performer (id_musician) VALUES(%s)"

    def __init__(self):
        pass

    def insert(self, id_band=None, id_musician=None):
        if id_band is not None and id_musician is not None:
            return
        if id_musician is not None:
            mysql_adapter.execute_with_params(self.__INSERT_IF_MUSICIAN_SQL, params=(id_musician,))
        else:
            mysql_adapter.execute_with_params(self.__INSERT_IF_BAND_SQL, params=(id_band,))
