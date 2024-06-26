import os
from otras_funciones import *
import math

# def solicitarNumeros():
#   global n1,n2  
#   n1=int(input("Numero #1: "))
#   n2=int(input("Numero #2: "))
  

# def operacionAritmetica(num1,num2,opcion):  
#     if opcion=="1" or opcion=="+" or opcion=="SUMA":
#       return f"{n1}+{n2}={n1+n2}"
#     elif opcion=="2" or opcion=="-" or opcion=="RESTA":
#      return f"{n1}-{n2}={n1-n2}"
#     elif opcion=="3" or opcion=="*" or opcion=="MULTIPLICACION":
#      return f"{n1}*{n2}={n1*n2}"
#     elif opcion=="4" or opcion=="/" or opcion=="DIVISION":
#      return f"{n1}/{n2}={n1/n2}"  
    
# def esperarTecla():
#   print("Oprima cualquier tecla para continuar ...")
#   input()

opcion=True 
   
while opcion:
 os.system("clear")
 print("\n\t..:: CALCULADORA BÁSICA ::..\n 1.- Suma \n 2.- Resta\n 3.- Multiplicación\n 4.- División\n 5.- Potencia\n 6.- Raíz Cuadrada\n 7.- SALIR") 

 opcion=input("\t Elige una opción: ").strip().upper()
 
if opcion in ["1", "2", "3", "4", "5", "6"]:
        solicitarNumeros()
        print(operacionAritmetica(n1, n2, opcion))

        input("Presiona Enter para continuar...")
elif opcion == "7" or opcion.upper() == "SALIR":
        print("Terminaste la ejecución del programa.")
        opcion = False
else:
  print("Opción no válida. Introduce un número del 1 al 7.")
  input("Presiona Enter para continuar...")
   