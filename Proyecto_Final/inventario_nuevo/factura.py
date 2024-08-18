from conexion import Conexion

class Factura:
    def __init__(self, id=None, pedido_id=None, empleado_id=None, fecha=None):
        self.id = id
        self.pedido_id = pedido_id
        self.empleado_id = empleado_id
        self.fecha = fecha

    def create(self):
        conn = Conexion()
        conn.open_connection()
        cursor = conn.get_cursor()
        query = """
        INSERT INTO Factura (pedido_id, empleado_id, fecha)
        VALUES (%s, %s, %s)
        """
        cursor.execute(query, (self.pedido_id, self.empleado_id, self.fecha))
        conn.conn.commit()
        conn.close_connection()
