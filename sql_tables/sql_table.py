class SQLTable:
    def generate_where(self, keys: list = []):
        if len(keys) == 0:
            return ""
        where_sql = ' where '
        conditions = []
        for key in keys:
            conditions.append('{}=%s'.format(key))
        return where_sql + " and ".join(conditions)