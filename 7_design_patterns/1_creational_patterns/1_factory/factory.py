from abc import ABC, abstractmethod
import pymysql
import psycopg2
import pandas as pd
import os

password = os.getenv("PASSWORD")
print(f"PASSWORD: {password}")

# Product Class
class DatabaseConnector(ABC):
    """
    Defines the common interface for all Databases that can be created by the factory.
    It's often abstract, meaning it can't be instantiated directly.
    """
    @abstractmethod
    def connect():
        pass


# Concrete Product-1
class MySQLConnector(DatabaseConnector):
    """
    Implementing the DatabaseConnector interface, defining specific behaviors for each type of connector.
    """
    def connect(self, **kwargs):
        try:
            return pymysql.connect(host=kwargs["host"],
                            port=kwargs["port"],
                            user=kwargs["user"],
                            password=kwargs["password"],
                            database=kwargs["database"])
        except Exception as ex:
            return f"Exception: {ex}"


# Concrete Product-2
class PostgresConnector(DatabaseConnector):
    """
    Implementing the DatabaseConnector interface, defining specific behaviors for each type of connector.
    """
    def connect(self, **kwargs):
        try:
            return psycopg2.connect(host=kwargs["host"],
                            port=kwargs["port"],
                            user=kwargs["user"],
                            password=kwargs["password"],
                            database=kwargs["database"])
        except Exception as ex:
            return f"Exception: {ex}"


# Factory class to create instances of concrete products
class DatabaseFactory:
    def create_connect(self, db_type):
        """
        Factory Method
        """
        if db_type == "MySQL":
            return MySQLConnector()
        elif db_type == "Postgres":
            return PostgresConnector()
        else:
            raise ValueError("Invalid Database Type")


# Client code that uses the factory to create objects
def main():
    db_obj = DatabaseFactory()

    mysql_connect = db_obj.create_connect("MySQL")
    mysql_connection = mysql_connect.connect(host="localhost", 
                                             port=3306, 
                                             user="admin", 
                                             password=password, 
                                             database="world")
    query = "SELECT * FROM city"
    data = pd.read_sql_query(query, mysql_connection)
    print(data)

    pg_connect = db_obj.create_connect("Postgres")
    pg_conn = pg_connect.connect(host="localhost", 
                                 port=5432,
                                 user="postgres", 
                                 password="password", 
                                 database="my_db")
    print(pg_conn)


if __name__ == "__main__":
    main()


        
    