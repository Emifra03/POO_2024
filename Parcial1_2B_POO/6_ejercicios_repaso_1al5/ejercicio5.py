#Hacer un programa que muestre todos los numeros entre 2 numeros que diga el usuario

num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))

# Asegurarse de que num1 es menor que num2
if num1 > num2:
    num1, num2 = num2, num1

# Mostrar los números entre num1 y num2
for num in range(num1 + 1, num2):
    print(num)