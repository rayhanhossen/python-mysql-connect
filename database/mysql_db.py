from mysql.connector import Error


class DatabaseOperation:
    def __init__(self, client):
        self.client = client

    def create_table(self, table_name):
        """

        :param table_name:
        """
        try:
            cursor = self.client.cursor()
            cursor.execute(table_name)

        except Error as e:
            print(f"Failed to create table in MySQL: {e}")

    def select_data_from_table(self, select_query):
        """

        :rtype: object
        """
        try:
            cursor = self.client.cursor()
            cursor.execute(select_query)
            records = cursor.fetchall()
            return records
        except Error as e:
            print("Error reading data from MySQL table", e)
