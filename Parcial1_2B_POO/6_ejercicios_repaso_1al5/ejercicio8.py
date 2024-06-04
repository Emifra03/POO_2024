#Hacer un programa que resuelva lo siguiente. ¿Cuanto es el X por ciento de X numero?


porcentaje = float(input("Introduce el porcentaje (por ejemplo, 20 para 20%): "))
numero = float(input("Introduce el número: "))

# Calcular el porcentaje del número
resultado = (porcentaje / 100) * numero

# Mostrar el resultado
print(f"{porcentaje}% de {numero} es {resultado}")