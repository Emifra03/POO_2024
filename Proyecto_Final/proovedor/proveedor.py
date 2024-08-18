from conexion import Conexion

class Proveedor:
    def __init__(self, id=None, nombre=None, contacto=None, direccion=None):
        self.id = id
        self.nombre = nombre
        self.contacto = contacto
        self.direccion = direccion

    def create(self):
        conn = Conexion()
        conn.open_connection()
        cursor = conn.get_cursor()
        query = """
        INSERT INTO Proveedor (nombre, contacto, direccion)
        VALUES (%s, %s, %s)
        """
        cursor.execute(query, (self.nombre, self.contacto, self.direccion))
        conn
