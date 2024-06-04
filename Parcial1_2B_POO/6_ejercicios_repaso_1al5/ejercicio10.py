#Crear un programa que solicite la calificacion de 15 alumnos e imprimir en pantalla cuantos aproboron y cuantos no aprobaron

# Inicializar contadores
aprobados = 0
reprobados = 0

# Solicitar las calificaciones de los 15 alumnos
for i in range(1, 16):
    calificacion = float(input(f"Introduce la calificación del alumno {i}: "))
    if calificacion >= 5:
        aprobados += 1
    else:
        reprobados += 1

# Mostrar el resultado
print(f"Aprobados: {aprobados}")
print(f"No Aprobados: {reprobados}")