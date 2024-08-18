from conexion import Conexion

class Producto:
    def __init__(self, id=None, nombre=None, tipo=None, precio=None):
        self.id = id
        self.nombre = nombre
        self.tipo = tipo
        self.precio = precio

    def create(self):
        conn = Conexion()
        conn.open_connection()
        cursor = conn.get_cursor()
        query = """
        INSERT INTO Producto (nombre, tipo, precio)
        VALUES (%s, %s, %s)
        """
        cursor.execute(query, (self.nombre, self.tipo, self.precio))
        conn.commit()
        conn.close_connection()

    def read(self, id):
        conn = Conexion()
        conn.open_connection()
        cursor = conn.get_cursor()
        query = "SELECT * FROM Producto WHERE id = %s"
        cursor.execute(query, (id,))
        result = cursor.fetchone()
        conn.close_connection()
        return result

    def update(self):
        conn = Conexion()
        conn.open_connection()
        cursor = conn.get_cursor()
        query = """
        UPDATE Producto
        SET nombre = %s, tipo = %s, precio = %s
        WHERE id = %s
        """
        cursor.execute(query, (self.nombre, self.tipo, self.precio, self.id))
        conn.commit()
        conn.close_connection()

    def delete(self, id):
        conn = Conexion()
        conn.open_connection()
        cursor = conn.get_cursor()
        query = "DELETE FROM Producto WHERE id = %s"
        cursor.execute(query, (id,))
        conn.commit()
        conn.close_connection()
