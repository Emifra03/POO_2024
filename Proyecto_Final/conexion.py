import mysql.connector

class Conexion:
    def __init__(self, host='localhost', user='root', password='', database='bakery_system'):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        self.cursor = None

    def open_connection(self):
        if self.connection is None or not self.connection.is_connected():
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
        self.cursor = self.connection.cursor()

    def close_connection(self):
        if self.cursor:
            self.cursor.close()
        if self.connection and self.connection.is_connected():
            self.connection.close()

    def get_cursor(self):
        if self.cursor is None:
            raise Exception("Connection is not open. Call open_connection() first.")
        return self.cursor

    def commit(self):
        if self.connection and self.connection.is_connected():
            self.connection.commit()
