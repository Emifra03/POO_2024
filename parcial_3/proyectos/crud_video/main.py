import getpass
from pasteles import Pasteles
from funciones import *


def menu_principal():
    while True:
        borrarPantalla()
        print("""
      .::  Menu Principal ::. 
          1.- Registro
          2.- Login
          3.- Salir 
          """)
        opcion = input("\t Elige una opción: ")

        if opcion == '1':
            borrarPantalla()
            print("\n \t ..:: Registro en el Sistema ::..")
            nombre = input("\t ¿Cual es tu nombre?: ")
            apellidos = input("\t ¿Cuales son tus apellidos?: ")
            email = input("\t Ingresa tu email: ")
            password = getpass.getpass("\t Ingresa tu contraseña: ")
            # Agregar código de registro
            esperarTecla()
        elif opcion == '2':
            borrarPantalla()
            print("\n \t ..:: Inicio de Sesión ::.. ")
            email = input("\t Ingresa tu E-mail: ")
            password = getpass.getpass("\t Ingresa tu Contraseña: ")
            # Agregar código de inicio de sesión
        elif opcion == '3':
            print("\n\t.. ¡Gracias Bye! ...")
            break
        else:
            print("\n \t \t Opción no válida. Intenta de nuevo.")
            esperarTecla()

def menu_notas(usuario_id, nombre, apellidos):
    pasteles = Pasteles()
    while True:
        borrarPantalla()
        print(f"\n \t \t \t Bienvenido {nombre} {apellidos}, has iniciado sesión ...")
        print("""
                  \n \t 
                      .::  Menu Notas ::. 
                  1.- Crear 
                  2.- Mostrar
                  3.- Cambiar
                  4.- Eliminar
                  5.- Salir 
                  """)
        opcion = input("\t\t Elige una opción: ")

        if opcion == '1':
            borrarPantalla()
            print(f"\n \t .:: Crear Nota ::. ")
            nombre = input("\tNombre del pastel: ")
            sabor = input("\tSabor del pastel: ")
            precio = float(input("\tPrecio del pastel: "))
            pasteles.create_pastel(nombre, sabor, precio)
            esperarTecla()
        elif opcion == '2':
            borrarPantalla()
            pasteles.read_pasteles()
            esperarTecla()
        elif opcion == '3':
            borrarPantalla()
            print(f"\n \t .:: {nombre} {apellidos}, vamos a modificar un Nota ::. \n")
            id = int(input("\t \t ID del pastel a actualizar: "))
            nombre = input("\t Nuevo nombre: ")
            sabor = input("\t Nuevo sabor: ")
            precio = float(input("\t Nuevo precio: "))
            pasteles.update_pastel(id, nombre, sabor, precio)
            esperarTecla()
        elif opcion == '4':
            borrarPantalla()
            print(f"\n \t .:: {nombre} {apellidos}, vamos a borrar un Nota ::. \n")
            id = int(input("\t \t ID del pastel a eliminar: "))
            pasteles.delete_pastel(id)
            esperarTecla()
        elif opcion == '5':
            break
        else:
            print("\n \t \t Opción no válida. Intenta de nuevo.")
            esperarTecla()

if __name__ == "__main__":
    menu_principal()
