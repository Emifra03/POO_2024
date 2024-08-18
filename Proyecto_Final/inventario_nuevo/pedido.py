from conexion import Conexion

class Pedido:
    def __init__(self, id=None, fecha=None, detalle_Pedido=None, cantidad=None, empleado_id=None):
        self.id = id
        self.fecha = fecha
        self.detalle_Pedido = detalle_Pedido
        self.cantidad = cantidad
        self.empleado_id = empleado_id

    def create(self):
        conn = Conexion()
        conn.open_connection()
        cursor = conn.get_cursor()
        query = """
        INSERT INTO Pedido (fecha, detalle_Pedido, cantidad, empleado_id)
        VALUES (%s, %s, %s, %s)
        """
        cursor.execute(query, (self.fecha, self.detalle_Pedido, self.cantidad, self.empleado_id))
        conn.conn.commit()
        conn.close_connection()

    def read(self, id):
        conn = Conexion()
        conn.open_connection()
        cursor = conn.get_cursor()
        query = "SELECT * FROM Pedido WHERE id = %s"
        cursor.execute(query, (id,))
        result = cursor.fetchone()
        conn.close_connection()
        return result

    def update(self):
        conn = Conexion()
        conn.open_connection()
        cursor = conn.get_cursor()
        query = """
        UPDATE Pedido
        SET fecha = %s, detalle_Pedido = %s, cantidad = %s, empleado_id = %s
        WHERE id = %s
        """
        cursor.execute(query, (self.fecha, self.detalle_Pedido, self.cantidad, self.empleado_id, self.id))
        conn.conn.commit()
        conn.close_connection()

    def delete(self, id):
        conn = Conexion()
        conn.open_connection()
        cursor = conn.get_cursor()
        query = "DELETE FROM Pedido WHERE id = %s"
        cursor.execute(query, (id,))
        conn.conn.commit()
        conn.close_connection()
