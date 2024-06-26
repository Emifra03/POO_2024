# Hacer un programa que tenga una lista de 8 numeros enteros y realice lo siguiente: 

# a.- Recorrer la lista y mostrarla
# b.- hacer una funcion que recorra la lista de numeros y devuelva un string
# c.- ordenarla y mostrarla
# d.- mostrar su longitud
# e.- buscar algun elemento que el usuario pida por teclado

lista=[]

def mostar_inicio():
 print("\n Menu de inicio")
print("Mostar opciones")


def agregar_numeros(lista_numeros, numeros):
    lista_numeros.append(numeros)
    print(f"los '{numeros}' han sido agregados.")
    
def lista_a_string(lista):
    return ', '.join(map(str, lista))

print("\nLongitud de la lista:")
print(len(lista))

elemento_a_buscar = int(input("\nIngresa un número a buscar en la lista: "))
if elemento_a_buscar in lista:
    print(f"El número {elemento_a_buscar} se encuentra en la lista, en la posición {lista.index(elemento_a_buscar)}.")
else:
    print(f"El número {elemento_a_buscar} no se encuentra en la lista.")