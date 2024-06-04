# Escribir un programa que muestre los cuadrados 
#(un numero multiplicado por si mismo) de los 60 primeros 
#numeros naturales. Resolverlo con while y for
#

num = 1
while num <= 60:
    print(f"El cuadrado de {num} es {num * num}")
    num += 1


num=1
for num in range (1,61):
    print(f"el cuadrado de {num} es {num * num}")
    