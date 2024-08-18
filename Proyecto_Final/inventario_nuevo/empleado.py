from conexion import Conexion

class Empleado:
    def __init__(self, id=None, nombre=None, email=None, puesto=None, contrasena=None):
        self.id = id
        self.nombre = nombre
        self.email = email
        self.puesto = puesto
        self.contrasena = contrasena

    def create(self):
        conn = Conexion()
        conn.open_connection()
        cursor = conn.get_cursor()
        query = """
        INSERT INTO Empleado (nombre, email, puesto, contrasena)
        VALUES (%s, %s, %s, %s)
        """
        cursor.execute(query, (self.nombre, self.email, self.puesto, self.contrasena))
        conn.conn.commit()
        conn.close_connection()

    @staticmethod
    def login(email, password):
        conn = Conexion()
        conn.open_connection()
        cursor = conn.get_cursor()
        query = "SELECT * FROM Empleado WHERE email = %s AND contrasena = %s"
        cursor.execute(query, (email, password))
        result = cursor.fetchone()
        conn.close_connection()
        return result is not None
