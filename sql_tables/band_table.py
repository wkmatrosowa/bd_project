from mysql_helper import mysql_helper


class BandTable:

    __name = 'band'
    __INSERT_SQL = "INSERT INTO band (bandname, yearoffoundation) VALUES (%s, %s)"
    __UPDATE_SQL = ""
    __DELETE_SQL = ""
    __FIND_SQL = ""

    def __init__(self):
        pass

    def insert(self, bandname: str = "", yearoffoundation: str = ""):
        mysql_helper.execute_with_params(query=self.__INSERT_SQL, params=(bandname, yearoffoundation))

    def update(self):
        pass

    def delete(self):
        pass

    def find(self):
        pass