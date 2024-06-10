import os

from listas import *
def mostrar_menu():
    print("\n.:: Gestión de Películas ::.")
    print("1. Agregar película")
    print("2. Remover película")
    print("3. Consultar películas")
    print("4. Salir")

    lista_peliculas = []
    while True:
        mostrar_menu()
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            pelicula = input("Ingrese el nombre de la película a agregar: ")
            list.agregar_pelicula(lista_peliculas, pelicula)
        elif opcion == "2":
            pelicula = input("Ingrese el nombre de la película a remover: ")
            list.remover_pelicula(lista_peliculas, pelicula)
        elif opcion == "3":
            list.consultar_peliculas(lista_peliculas)
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor, intente de nuevo.")

