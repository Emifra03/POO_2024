import mysql.connector
from mysql.connector import Error

class ConexionDB:
    def _init_(self):
        
        self.config = {
            'user': 'root',          
            'password': '',          
            'host': 'localhost',
            'database': 'agencia_autos_datos'
        }
    
    def conectar(self):
        try:
            conexion = mysql.connector.connect(**self.config)
            if conexion.is_connected():
                print("Conexión exitosa!")
                return conexion
        except Error as e:
            print(f"Error al conectar a MySQL: {e}")
            raise

    def cerrar_conexion(self, conexion):
        if conexion.is_connected():
            conexion.close()
            print("Conexión cerrada.")

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",  
        password="", 
        database="agencia_autos_datos"
    )