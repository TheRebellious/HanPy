import mysql.connector
from mysql.connector import (connection)
from mysql.connector import errorcode


class Databaseconnector:
    def __init__(self, User, Password, Host, Database):
        self.connection: mysql.connector.MySQLConnection = mysql.connector.MySQLConnection(
            user=User, password=Password, host=Host, database=Database)

    def get(self, table: str, colomn: str):
        cursor = self.connection.cursor()

        query = f"SELECT {colomn} FROM {table}"
        cursor.execute(query)

        returnList = []
        for x in cursor.fetchall():
            returnList.append(x)

        return returnList

    def insert(self, table: str, data: list):
        cursor = self.connection.cursor()

        query = f"INSERT INTO {table} VALUES ("
        for column in data:
            print(column, data.index(column))
            if type(column) == str:
                query += f"\'{column}\'"  # adds 'colomn'
            else:
                query += f"{column}"
            if not data.index(column) == len(data)-1:
                query += ","
            else:
                query += ")"
        print(query[len(query)-1:])
        if query[len(query)-1:] != ")":
            query = query[:len(query)-1] + ")"
        print(query)
        try:
            cursor.execute(query)
        except Exception as e:
            print(e)
        self.connection.commit()

    def update(self, table: str, column: str, data: str, idKey: str, locker: int):
        cursor = self.connection.cursor()

        query = f"UPDATE {table} SET {column} = {data} WHERE {idKey} = {locker} "
        print(query)
        try:
            cursor.execute(query)

            self.connection.commit()
        except Exception as e:
            print(e)
