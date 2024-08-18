from conexion import Conexion

class Factura:
    def __init__(self, id=None, fecha=None, total=None, pedido_id=None, empleado_id=None):
        self.id = id
        self.fecha = fecha
        self.total = total
        self.pedido_id = pedido_id
        self.empleado_id = empleado_id

    def create(self):
        conn = Conexion()
        conn.open_connection()
        cursor = conn.get_cursor()
        query = """
        INSERT INTO Factura (fecha, total, pedido_id, empleado_id)
        VALUES (%s, %s, %s, %s)
        """
        cursor.execute(query, (self.fecha, self.total, self.pedido_id, self.empleado_id))
        conn.commit()
        conn.close_connection()

    def read(self, id):
        conn = Conexion()
        conn.open_connection()
        cursor = conn.get_cursor()
        query = "SELECT * FROM Factura WHERE id = %s"
        cursor.execute(query, (id,))
        result = cursor.fetchone()
        conn.close_connection()
        return result

    def update(self):
        conn = Conexion()
        conn.open_connection()
        cursor = conn.get_cursor()
        query = """
        UPDATE Factura
        SET fecha = %s, total = %s, pedido_id = %s, empleado_id = %s
        WHERE id = %s
        """
        cursor.execute(query, (self.fecha, self.total, self.pedido_id, self.empleado_id, self.id))
        conn.commit()
        conn.close_connection()

    def delete(self, id):
        conn = Conexion()
        conn.open_connection()
        cursor = conn.get_cursor()
        query = "DELETE FROM Factura WHERE id = %s"
        cursor.execute(query, (id,))
        conn.commit()
        conn.close_connection()

    def generar(self):
        if self.pedido_id:
            conn = Conexion()
            conn.open_connection()
            cursor = conn.get_cursor()

            # Suponiendo que la factura se genera a partir del pedido
            cursor.execute("SELECT * FROM Pedido WHERE id = %s", (self.pedido_id,))
            pedido = cursor.fetchone()

            if pedido:
                factura_detalle = f"Factura para el pedido ID: {self.pedido_id}\n"
                factura_detalle += f"Fecha: {pedido[1]}\nDetalle: {pedido[2]}\nCantidad: {pedido[3]}\n"

                # Puedes guardar la factura en la base de datos o en un archivo
                # Aquí solo la imprimimos como ejemplo
                print(factura_detalle)
                
                # Commit de cualquier cambio si se hace en la base de datos
                self.create()
            else:
                print("Pedido no encontrado")

            cursor.close()
            conn.close()
        else:
            print("ID de pedido no proporcionado")



