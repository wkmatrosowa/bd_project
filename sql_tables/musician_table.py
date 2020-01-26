from mysql_helper import mysql_helper


class MusicianTable:

    __name = 'musician'
    __INSERT_SQL = "INSERT INTO musician (firstname, surname, specialization) VALUES (%s, %s, %s)"
    __UPDATE_SQL = ""
    __DELETE_SQL = ""
    __FIND_SQL = ""

    def __init__(self):
        pass

    def insert(self, firstname: str = "", surname: str = "", specialization: str = ""):
        mysql_helper.execute_with_params(query=self.__INSERT_SQL, params=(firstname, surname, specialization))

    def update(self):
        pass

    def delete(self):
        pass

    def find(self):
        pass