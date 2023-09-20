import mysql.connector


class dbConnector:
    mydb: mysql.connector.MySQLConnection

    def __init__(self, dbhost, dbpassword, dbname):
        self.dbname = dbname
        self.mydb: mysql.connector.MySQLConnection = mysql.connector.connect(
            host=dbhost,
            user=dbhost,
            password=dbpassword,
            database=dbname
        )
        self.con = self.mydb.cursor()
        print("----------------------\ndb connected\n----------------------")

    def fetchAllData(self, table: str):
        self.con.execute("SELECT * FROM " + table)

        rs = self.con.fetchall()

        for x in rs:
            print(x)

    def insertData(self, table, data):
        query = "INSERT INTO " + self.dbname + "." + table
        self.con.execute(query, data)
