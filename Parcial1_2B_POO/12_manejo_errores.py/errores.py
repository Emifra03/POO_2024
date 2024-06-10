#Los errores en la ejecucion en un lenguaje de programacion se presentan cuando existe una anomalia o error dentro de la ejecucion del codigo, lo cual provoca que se detenga la ejecucion del SW. Con el control y manejo de excepciones sera posible minimizar o evitar la interrupcion del programa debido a una excepcion.

#Ejemplo 1 cuando una variable no se genera 

# try:
#   nombre=input("Introduce el nombre de una persona:  ")
#   if len(nombre)>0:
#     nombre_usuario="El nombre completo del usuario es: " + nombre
#     print(nombre_usuario)
# except:
#    print("Es necesario introducir un nombre de usurario... verifica por favor")

# x=3+4
# print("El valor de c es: " + str(x))

#Ejemplo 2 cuando se solicita un numero y se ingresa otra cosa 

# try:
#  numero=int(input("Ingrese un numero entero :"))
#  if numero>0:
#     print("Soy un numero entero positivo: ")
#  elif numero==0:
#     print("Soy un numero entero neutro: ")
#  else:
#     print("Soy un numero entero negativo: ") 
# except:
#    print("Introduce un numero entero")

#Ejemplo 3 Cuando se generan multiples excepciones

try:
    numero=int(input("Introduce un numero: "))

    print("El cuadrado del numero es:"+str(numero+numero))

except ValueError:
    print("Introduce un valor numerico entero:")

except TypeError:
    print("Se debe convertir el numero entero:")

else: 
    print("No se presentaron errores de ejecucion")
finally:
    print("Termine la ejecucion")