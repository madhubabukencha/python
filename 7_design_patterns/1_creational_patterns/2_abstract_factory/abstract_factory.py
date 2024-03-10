"""
The abstract factory design pattern is used to provide an interface
for creating families of related or dependent objects without specifying
their concrete classes. In the context of a database use case in Python,
let's consider a scenario where you need to connect to different types
of databases (e.g., MySQL, PostgresSQL) and perform basic operations like
querying and inserting data.
"""
from abc import ABC, abstractmethod
import pymysql
import psycopg2
import pandas as pd
import os


class DatabaseConnection(ABC):
    """
    Abstract Product-1:
    This is an abstract/interface product class for Database connection
    """
    @abstractmethod
    def connect(self):
        pass


class MySQLConnection(DatabaseConnection):
    """
    Concrete Product-1
    This is a concrete product class for making MySQL connection
    """
    def connect(self, **kwargs):
        try:
            print("Connecting Postgres Server")
            return pymysql.connect(host=kwargs["host"],
                                   port=kwargs["port"],
                                   user=kwargs["user"],
                                   password=kwargs["password"],
                                   database=kwargs["database"])
        except Exception as ex:
            return f"Exception: {ex}"


class PostgresConnector(DatabaseConnection):
    """
    Concrete Product-1
    This is a concrete product class for making Postgres connection
    """
    def connect(self, **kwargs):
        try:
            print("Connecting Postgres Server")
            return psycopg2.connect(host=kwargs["host"],
                                    port=kwargs["port"],
                                    user=kwargs["user"],
                                    password=kwargs["password"],
                                    database=kwargs["database"])
        except Exception as ex:
            return f"Exception: {ex}"


class QueryExecutor(ABC):
    """
    Abstract Product-2
    This is an abstract/interface product class for query execution.
    """
    @abstractmethod
    def execute_query(self, database_connection, query: str):
        pass


class MySQLQueryExecutor(QueryExecutor):
    """
    Concrete Product-2
    This is a concrete product class for making MySQL query Execution
    """
    def execute_query(self, database_connection, query: str):
        data = pd.read_sql_query(query, database_connection)
        print(data)


class PostgresQueryExecutor(QueryExecutor):
    """
    Concrete Product-2
    This is a concrete product class for making Postgres query Execution
    """
    def execute_query(self, database_connection, query: str):
        data = pd.read_sql_query(query, database_connection)
        print(data)


class DatabaseFactory(ABC):
    """
    Abstract Factory
    This is an abstract factory for Database Factory.
    It is used for creating families of related or dependent objects
    without specifying their concrete classes.
    """
    @abstractmethod
    def create_connection(self):
        pass

    @abstractmethod
    def create_query_executor(self):
        pass


class MySQLFactory(DatabaseFactory):
    """
    Concrete Product
    Implementation of Abstract Factory
    """
    def create_connection(self):
        return MySQLConnection()

    def create_query_executor(self):
        return MySQLQueryExecutor()


class PostgresFactory(DatabaseFactory):
    """
    Concrete Product
    Implementation of Abstract Factory
    """
    def create_connection(self):
        return PostgresConnector()

    def create_query_executor(self):
        return PostgresQueryExecutor()


class DataBaseClient:
    def __init__(self, *, factory, connection_credentials, query):
        self.factory = factory
        self.connection_credentials = connection_credentials
        self.query = query

    def perform_database_operations(self):
        connection_obj = self.factory.create_connection()
        db_connection = connection_obj.connect(**self.connection_credentials)

        query_executor = self.factory.create_query_executor()
        query_executor.execute_query(db_connection, self.query)


if __name__ == "__main__":
    password = os.getenv("PASSWORD")
    # print(f"PASSWORD: {password}")

    # Performing mysql operation
    mysql_cred = dict(host="localhost", port=3306, user="admin", password=password, database="world")
    my_query = "SELECT * FROM city"
    mysql_factory = MySQLFactory()
    mysql_client = DataBaseClient(factory=mysql_factory,
                                  connection_credentials=mysql_cred,
                                  query=my_query)
    mysql_client.perform_database_operations()

    # TODO: If you have postgres credential them implement that here like above
