#Hacer un programa que muestre todos los numeros impares entre 2 numeros que decida el usuario

num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))

# Asegurarse de que num1 es menor que num2
if num1 > num2:
    num1, num2 = num2, num1

# Mostrar los números impares entre num1 y num2
for num in range(num1 + 1, num2):
    if num % 2 != 0:
        print(num)