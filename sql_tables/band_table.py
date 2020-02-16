from mysql_helper import mysql_helper


class BandTable:

    __name = 'band'
    __INSERT_SQL = "INSERT INTO band (bandname, yearoffoundation) VALUES (%s, %s)"
    __UPDATE_SQL = ""
    __DELETE_SQL = ""
    __SELECT_SQL = "SELECT * FROM band"
    allowable_keys = ['id', 'bandname', 'yearoffoundation']

    def __init__(self):
        pass

    def insert(self, bandname: str = "", yearoffoundation: str = ""):
        mysql_helper.execute_with_params(query=self.__INSERT_SQL, params=(bandname, yearoffoundation))

    def update(self):
        pass

    def delete(self):
        pass

    def find(self, request: dict):
        return mysql_helper.select(self.__SELECT_SQL + self.generate_where(request.keys()), tuple(request.values()))

    def generate_where(self, keys: list = []):
        if len(keys) == 0:
            return ""
        where_sql = ' where '
        conditions = []
        for key in keys:
            conditions.append('{}=%s'.format(key))
        return where_sql + " and ".join(conditions)