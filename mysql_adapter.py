import mysql.connector

from sql_queries.table_creation_queries import table_creation_queries


class MySQLAdapter:

    def __init__(self, user="root", password=""):
        self.__mydb = mysql.connector.connect(
            host="localhost",
            user=user,
            passwd=password
        )
        self.__cursor = self.__mydb.cursor()

    def create_db(self, name="discography"):
        self.__cursor.execute("CREATE DATABASE IF NOT EXISTS {}".format(name))
        self.__mydb.database = name

    def create_all_tables(self, queries=[]):
        for query in queries:
            self.__cursor.execute(query)

    def execute(self, query: str):
        self.__cursor.execute(query)
        self.__mydb.commit()

    def execute_with_params(self, query: str, params: tuple = ()):
        self.__cursor.execute(query, params=params)
        self.__mydb.commit()

    def select(self, query: str, params: tuple = ()):
        self.__cursor.execute(query, params=params)
        return self.__cursor.fetchall()

    def inserted_id(self):
        return self.__cursor.lastrowid


mysql_adapter = MySQLAdapter()
mysql_adapter.create_db()
mysql_adapter.create_all_tables(table_creation_queries)
