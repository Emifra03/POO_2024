import math


def solicitarNumeros():
  #global n1,n2  
  n1=int(input("Numero #1: "))
  n2=int(input("Numero #2: "))
  return n1,n2

def operacionAritmetica(n1, n2, opcion):  
    if opcion == "1" or opcion == "+" or opcion == "SUMA":
        return f"{n1} + {n2} = {n1 + n2}"
    elif opcion == "2" or opcion == "-" or opcion == "RESTA":
        return f"{n1} - {n2} = {n1 - n2}"
    elif opcion == "3" or opcion == "*" or opcion == "MULTIPLICACION":
        return f"{n1} * {n2} = {n1 * n2}"
    elif opcion == "4" or opcion == "/" or opcion == "DIVISION":
        if n2 == 0:
            return "No se puede dividir por cero."
        else:
            return f"{n1} / {n2} = {n1 / n2}"
    elif opcion == "5" or opcion == "POTENCIA":
        return f"{n1} ^ {n2} = {n1 ** n2}"
    elif opcion == "6" or opcion == "RAIZ":
        if n1 < 0:
            return "No se puede calcular la raíz cuadrada de un número negativo."

        else:
            return f"Raíz cuadrada de {n1} = {math.sqrt(n1)}"
    elif opcion == "7" or opcion.upper() == "SALIR":
        return "Salir"
        
    else:
      return "Opción no válida"


    
def esperarTecla():
  print("Oprima cualquier tecla para continuar ...")
  input()