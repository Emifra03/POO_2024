"""""
list (array)
Son colecciones o conjunto de datos/valores bajo un mismo nombre, para acceder a los valores sehace con un indice numerico  

Nota: sus valores si son modificables

La lista es una colección ordenada y modificable 
Permite miembros duplicados

"""
# Ejeplo 1 crear una lsita de nuemrios e imprimir el contenido 

numeros=[23,34]
print(numeros)


#Recorrer la lista con un ciclo for 
for i in numeros:
    print(i)

#Recorrer la lista con un ciclo while

i=0
tamanio=len (numeros)
print (tamanio) 
i=0
while i<=len(numeros)-1:
    print(numeros[i]) 
    i+=1

#Ejemplo 32 crear una lista de palabras y posteriormente buscaer la coincidencia de una palabra 

palabras=["hola,saludos, america, azul"] 
palabras_buscar=input("Ingresa una palabra a buscar :")

for i in palabras:
  if i==palabras_buscar:
     print(f"se encontro la palabra a buscar en la posicion {palabras.index}")