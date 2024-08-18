from conexionBD import *
import getpass
import mysql.connector

usuarios = {}

def registrar_usuario():
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    correo = input("Correo: ")
    telefono = input("Número de teléfono: ")
    password = getpass.getpass("Contraseña: ")

    conn = conectar()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO usuarios (nombre, apellido, correo, telefono, contrasena) VALUES (%s, %s, %s, %s, %s)",
            (nombre, apellido, correo, telefono, password)
        )
        conn.commit()
        print("Registro exitoso.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

def iniciar_sesion():
    correo = input("Correo: ")
    password = getpass.getpass("Contrasena: ")

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT nombre, apellido FROM usuarios WHERE correo = %s AND contrasena = %s",
        (correo, password)
    )
    usuario = cursor.fetchone()

    cursor.close()
    conn.close()

    if usuario:
        print(f"Bienvenido, {usuario[0]} {usuario[1]}!")
        return True
    else:
        print("Correo o contrasena incorrectos.")
        return False