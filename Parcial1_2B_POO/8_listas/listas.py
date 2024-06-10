# """""
# list (array)
# Son colecciones o conjunto de datos/valores bajo un mismo nombre, para acceder a los valores sehace con un indice numerico  

# Nota: sus valores si son modificables

# La lista es una colección ordenada y modificable 
# Permite miembros duplicados

# """
# # Ejeplo 1 crear una lsita de nuemrios e imprimir el contenido 

# from itertools import islice


# numeros=[23,34]
# print(numeros)


# #Recorrer la lista con un ciclo for 
# for i in numeros:
#     print(i)

# #Recorrer la lista con un ciclo while

# i=0
# tamanio=len (numeros)
# print (tamanio) 
# i=0
# while i<=len(numeros)-1:
#     print(numeros[i]) 
#     i+=1

# #Ejemplo 32 crear una lista de palabras y posteriormente buscaer la coincidencia de una palabra 

# palabras=["hola,saludos, america, azul"] 
# print(palabras)

# palabras_buscar=input("Ingresa una palabra a buscar :")

# encontro=False

# # for i in palabras:
# #   if palabras[i]==palabras_buscar:
# #      print(f"se encontro la {palabras_buscar} en la posicion {palabras.index(i)}")
# #      encontro=True

# # if not encontro:
# #    print("no se encontro la palabra a buscar")

# i=0
# while i<=len(palabras):
#     if palabras[i]==palabras_buscar:
#         print(f"se encontro la {palabras_buscar} en la posicion {i}")
#         encontro=True
#         i+=1




# numeros[23,34,23]
# print(numeros)

# #agregar un elemento
# numeros.append(100)
# print(numeros)
# numeros.insert(3,200)
# print(numeros)

# #eliminar un elemento
# numeros.remove(100) # indicar el elemento a borrar 
# print(numeros)
# numeros.pop(2) #indicar la posicion del elemento a borrar
# print(numeros)

#ejemplo 4 crear una lista multilinea (matriz) para agregar los nombres y numeros telefonicos 

# agenda=[
#     ["Carlos",6181234567],
#     ["Leo",6671234567],
#     ["Carlos",6181234567],
#     ["Sebastian",6182341234],
#     ["Pedro",61711236789]
#     ]

# print(agenda)

# for i in agenda:
#     print(f"{agenda.index(i)+1}.-{i}")

#ejemplo 5 crear un programa que permita gestionar (administrar) peliuculas, colocar un menu de opciones para agregar, remover, consultar peliculas.
#Notas:
#1.- Utilizar funciones y mandar llamar desde otro archivo
#2.- Utilizar listas para almacenar los nombres de peliculas 


def agregar_pelicula(lista_peliculas, pelicula):
    """Agrega una película a la lista."""
    lista_peliculas.append(pelicula)
    print(f"La película '{pelicula}' ha sido agregada.")

def remover_pelicula(lista_peliculas, pelicula):
    """Remueve una película de la lista."""
    if pelicula in lista_peliculas:
        lista_peliculas.remove(pelicula)
        print(f"La película '{pelicula}' ha sido removida.")
    else:
        print(f"La película '{pelicula}' no se encuentra en la lista.")

def consultar_peliculas(lista_peliculas):
    """Muestra la lista de películas."""
    if lista_peliculas:
        print("Lista de películas:")
        for pelicula in lista_peliculas:
            print(f"- {pelicula}")
    else:
        print("No hay películas en la lista.")