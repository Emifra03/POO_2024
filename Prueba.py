try:
    # Código que puede causar una excepción
    resultado = 10 / 0
except ZeroDivisionError:
    # Código para manejar la excepción
    print("No se puede dividir por cero")
finally:
    # Código que se ejecutará sin importar si hubo una excepción o no
    print("Fin del manejo de excepciones")
