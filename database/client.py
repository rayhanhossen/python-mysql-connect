import mysql.connector
from decouple import config
from mysql.connector import Error


class MySQLClient:
    def __init__(self):
        self.host = config('DATABASE_HOST')
        self.database = config('DATABASE_NAME')
        self.port = config('DATABASE_PORT')
        self.user = config('DATABASE_USERNAME')
        self.password = config('DATABASE_PASSWORD')

    def connect(self):
        """
        Connect to the MySQL database
        :raise: Error while connecting to mysql
        :return: MySQL database connection
        :rtype: object
        """
        try:
            print(self.host, self.database, self.user, self.password)
            connection = mysql.connector.connect(host=self.host,
                                                 database=self.database,
                                                 port=self.port,
                                                 user=self.user,
                                                 password=self.password)

            if connection.is_connected():
                db_Info = connection.get_server_info()
                print("Connected to MySQL Server version ", db_Info)
                cursor = connection.cursor()
                cursor.execute("select database();")
                record = cursor.fetchone()
                print("You're connected to database: ", record)
                cursor.close()
            return connection

        except Error as e:
            print("Error while connecting to MySQL", e)
