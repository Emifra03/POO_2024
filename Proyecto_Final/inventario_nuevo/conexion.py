import psycopg2
from psycopg2 import sql

class Conexion:
    def __init__(self):
        self.conn = None
        self.cursor = None

    def open_connection(self):
        try:
            self.conn = psycopg2.connect(
                dbname="tu_basedatos",
                user="root",
                password="",
                host="localhost"
            )
            self.cursor = self.conn.cursor()
        except Exception as e:
            print(f"Error al conectar a la base de datos: {e}")

    def close_connection(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()

    def get_cursor(self):
        return self.cursor
