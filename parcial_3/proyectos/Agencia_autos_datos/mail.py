import os
import getpass
from conexionBD import *
from clientes.cliente import *
from auto.auto import *
from revisiones.revisione import *
from usuarios.usuarios import *
from funciones import *

def menu_autos():
    opciones = {
        '1': lambda: (
            Auto(
                input("Matrícula: "), 
                input("Marca: "), 
                int(input("Modelo: ")), 
                input("Color: "), 
                int(input("NIF del cliente (puede no existir en la tabla clientes): "))
            ).insertar(),
            print("Auto insertado exitosamente.")
        ),
        
        '2': lambda: print("\n".join(map(str, Auto.consultar()))),
        
        '3': lambda: (
            Auto.actualizar(
                input("Matrícula del auto a actualizar: "),
                input("Marca (dejar en blanco para no actualizar): ") or None,
                int(input("Modelo (dejar en blanco para no actualizar): ") or 0) or None,
                input("Color (dejar en blanco para no actualizar): ") or None,
                int(input("NIF del cliente (dejar en blanco para no actualizar): ") or 0) or None
            ),
            print("Auto actualizado exitosamente.")
        ),
        
        '4': lambda: (
            Auto.eliminar(input("Matrícula del auto a eliminar: ")),
            print("Auto eliminado exitosamente.")
        ),
    }

    while True:
        borrar_pantalla()
        print("\nGestión de Autos")
        print("1. Insertar Auto\n2. Consultar Autos\n3. Actualizar Auto\n4. Eliminar Auto\n5. Salir")
        opcion = input("Selecciona una opción: ")
        if opcion == '5': break
        opciones.get(opcion, lambda: print("Opción no válida."))()
        esperar_tecla()

def menu_clientes():
    opciones = {
        '1': lambda: (
            Cliente(
                int(input("NIF: ")), 
                input("Nombre: "), 
                input("Dirección: "), 
                input("Ciudad: "), 
                int(input("Teléfono: "))
            ).insertar(),
            print("Cliente insertado exitosamente.")
        ),
        
        '2': lambda: print("\n".join(map(str, Cliente.consultar()))),
        
        '3': lambda: (
            Cliente.actualizar(
                int(input("NIF del cliente a actualizar: ")),
                input("Nombre (dejar en blanco para no actualizar): ") or None,
                input("Dirección (dejar en blanco para no actualizar): ") or None,
                input("Ciudad (dejar en blanco para no actualizar): ") or None,
                int(input("Teléfono (dejar en blanco para no actualizar): ") or 0) or None
            ),
            print("Cliente actualizado exitosamente.")
        ),
        
        '4': lambda: (
            Cliente.eliminar(int(input("NIF del cliente a eliminar: "))),
            print("Cliente eliminado exitosamente.")
        ),
    }

    while True:
        borrar_pantalla()
        print("\nGestión de Clientes")
        print("1. Insertar Cliente\n2. Consultar Clientes\n3. Actualizar Cliente\n4. Eliminar Cliente\n5. Salir")
        opcion = input("Selecciona una opción: ")
        if opcion == '5': break
        opciones.get(opcion, lambda: print("Opción no válida."))()
        esperar_tecla()

def menu_revisiones():
    opciones = {
        '1': lambda: (
            Revision(
                int(input("Número de revisión: ")), 
                input("Cambio de filtro (S/N): "), 
                input("Cambio de aceite (S/N): "), 
                input("Cambio de frenos (S/N): "), 
                input("Otros detalles: "), 
                input("Matrícula del auto: ")
            ).insertar(),
            print("Revisión insertada exitosamente.")
        ),
        
        '2': lambda: print("\n".join(map(str, Revision.consultar()))),
        
        '3': lambda: (
            Revision.actualizar(
                int(input("Número de revisión a actualizar: ")),
                input("Cambio de filtro (dejar en blanco para no actualizar): ") or None,
                input("Cambio de aceite (dejar en blanco para no actualizar): ") or None,
                input("Cambio de frenos (dejar en blanco para no actualizar): ") or None,
                input("Otros detalles (dejar en blanco para no actualizar): ") or None,
                input("Matrícula del auto (dejar en blanco para no actualizar): ") or None
            ),
            print("Revisión actualizada exitosamente.")
        ),
        
        '4': lambda: (
            Revision.eliminar(int(input("Número de revisión a eliminar: "))),
            print("Revisión eliminada exitosamente.")
        ),
    }

    while True:
        borrar_pantalla()
        print("\nGestión de Revisiones")
        print("1. Insertar Revisión\n2. Consultar Revisiones\n3. Actualizar Revisión\n4. Eliminar Revisión\n5. Salir")
        opcion = input("Selecciona una opción: ")
        if opcion == '5': break
        opciones.get(opcion, lambda: print("Opción no válida."))()
        esperar_tecla()

def menu_principal():
    menus = {
        '1': menu_autos,
        '2': menu_clientes,
        '3': menu_revisiones,
    }

    while True:
        borrar_pantalla()
        print("\nMenú Principal")
        print("1. Gestionar Autos\n2. Gestionar Clientes\n3. Gestionar Revisiones\n4. Salir")
        opcion = input("Selecciona una opción: ")
        if opcion == '4': break
        menus.get(opcion, lambda: print("Opción no válida."))()
        esperar_tecla()

if __name__ == "_main_":
    while True:
        borrar_pantalla()
        print("\nBienvenido al sistema de gestión")
        print("1. Registrarse\n2. Iniciar sesión\n3. Salir")
        opcion = input("Selecciona una opción: ")
        borrar_pantalla()
        if opcion == '1':
            registrar_usuario()
            borrar_pantalla()  
        elif opcion == '2':
            if iniciar_sesion():
                menu_principal()
                borrar_pantalla()
        elif opcion == '3':
            break
        else:
            print("Opción no válida.")
        esperar_tecla()