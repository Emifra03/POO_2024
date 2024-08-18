from conexion import Conexion
import hashlib

class Empleado:
    def __init__(self, id=None, nombre=None, email=None, puesto=None, contrasena=None):
        self.id = id
        self.nombre = nombre
        self.email = email
        self.puesto = puesto
        self.contrasena = contrasena

    def _hash_password(self, password):
        """Hash the password using SHA-256"""
        return hashlib.sha256(password.encode()).hexdigest()

    def create(self):
        conn = Conexion()
        conn.open_connection()
        cursor = conn.get_cursor()
        hashed_password = self._hash_password(self.contrasena)
        query = """
        INSERT INTO Empleado (nombre, email, puesto, contrasena)
        VALUES (%s, %s, %s, %s)
        """
        cursor.execute(query, (self.nombre, self.email, self.puesto, hashed_password))
        conn.commit()
        conn.close_connection()

    def read(self, id):
        conn = Conexion()
        conn.open_connection()
        cursor = conn.get_cursor()
        query = "SELECT * FROM Empleado WHERE id = %s"
        cursor.execute(query, (id,))
        result = cursor.fetchone()
        conn.close_connection()
        return result

    def update(self):
        conn = Conexion()
        conn.open_connection()
        cursor = conn.get_cursor()
        hashed_password = self._hash_password(self.contraseña)
        query = """
        UPDATE Empleado
        SET nombre = %s, email = %s, puesto = %s, contrasena = %s
        WHERE id = %s
        """
        cursor.execute(query, (self.nombre, self.email, self.puesto, hashed_password, self.id))
        conn.commit()
        conn.close_connection()

    def delete(self, id):
        conn = Conexion()
        conn.open_connection()
        cursor = conn.get_cursor()
        query = "DELETE FROM Empleado WHERE id = %s"
        cursor.execute(query, (id,))
        conn.commit()
        conn.close_connection()

    @staticmethod
    def login(email, contrasena):
        conn = Conexion()
        conn.open_connection()
        cursor = conn.get_cursor()
        hashed_password = hashlib.sha256(contrasena.encode()).hexdigest()
        query = """
        SELECT * FROM Empleado
        WHERE email = %s AND contrasena = %s
        """
        cursor.execute(query, (email, hashed_password))
        result = cursor.fetchone()
        conn.close_connection()
        return result is not None
