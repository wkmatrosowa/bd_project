from mysql_adapter import mysql_adapter


class SQLTable:
    def generate_where(self, keys: list = []):
        if len(keys) == 0:
            return ""
        where_sql = ' where '
        conditions = []
        for key in keys:
            conditions.append('{}=%s'.format(key))
        return where_sql + " and ".join(conditions)

    def inserted_id(self):
        return mysql_adapter.inserted_id()