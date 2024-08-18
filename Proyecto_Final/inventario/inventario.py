from conexion import Conexion

class Inventario:
    def __init__(self, id=None, producto_id=None, stockActual=None, stockMin=None, stockMax=None, fecha_entrada=None):
        self.id = id
        self.producto_id = producto_id
        self.stockActual = stockActual
        self.stockMin = stockMin
        self.stockMax = stockMax
        self.fecha_entrada = fecha_entrada

    def create(self):
        conn = Conexion()
        conn.open_connection()
        cursor = conn.get_cursor()
        query = """
        INSERT INTO Inventario (producto_id, stockActual, stockMin, stockMax, fecha_entrada)
        VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(query, (self.producto_id, self.stockActual, self.stockMin, self.stockMax, self.fecha_entrada))
        conn.commit()
        conn.close_connection()

    def read(self, id):
        conn = Conexion()
        conn.open_connection()
        cursor = conn.get_cursor()
        query = "SELECT * FROM Inventario WHERE id = %s"
        cursor.execute(query, (id,))
        result = cursor.fetchone()
        conn.close_connection()
        return result

    def update(self):
        conn = Conexion()
        conn.open_connection()
        cursor = conn.get_cursor()
        query = """
        UPDATE Inventario
        SET producto_id = %s, stockActual = %s, stockMin = %s, stockMax = %s, fecha_entrada = %s
        WHERE id = %s
        """
        cursor.execute(query, (self.producto_id, self.stockActual, self.stockMin, self.stockMax, self.fecha_entrada, self.id))
        conn.commit()
        conn.close_connection()

    def delete(self, id):
        conn = Conexion()
        conn.open_connection()
        cursor = conn.get_cursor()
        query = "DELETE FROM Inventario WHERE id = %s"
        cursor.execute(query, (id,))
        conn.commit()
        conn.close_connection()
