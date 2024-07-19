from prueba import *

# Crear instancia de Veterinaria
veterinaria = Veterinaria("VetExpress", "123 Calle Falsa", "123456789")

# Crear instancias de Animal
animal1 = Animal("Firulais", "Labrador", 5, "Juan Pérez")
animal2 = Animal("Michi", "Siames", 3, "María García")

# Añadir animales a la veterinaria
veterinaria.get_animales().append(animal1)
veterinaria.get_animales().append(animal2)

# Crear instancias de Cliente
cliente1 = Cliente("Juan Pérez", "456 Calle Verdadera", "987654321")
cliente2 = Cliente("María García", "789 Calle Imaginaria", "654321987")

# Añadir clientes a la veterinaria
veterinaria.get_clientes().append(cliente1)
veterinaria.get_clientes().append(cliente2)

# Crear instancias de Empleado
empleado1 = Empleado("Ana López", "Veterinario", 1500)
empleado2 = Empleado("Carlos Ruiz", "Asistente", 900)

# Añadir empleados a la veterinaria
veterinaria.get_empleados().append(empleado1)
veterinaria.get_empleados().append(empleado2)

# Crear instancias de Servicio
servicio1 = Servicio("Consulta General", 50)
servicio2 = Servicio("Vacunación", 30)

# Añadir servicios a la veterinaria
veterinaria.get_servicios().append(servicio1)
veterinaria.get_servicios().append(servicio2)

# Crear instancias de Cita
cita1 = Cita("2024-07-01", "10:00 AM", animal1, cliente1, servicio1)
cita2 = Cita("2024-07-02", "11:00 AM", animal2, cliente2, servicio2)

# Añadir citas a la veterinaria
veterinaria.get_citas().append(cita1)
veterinaria.get_citas().append(cita2)

# Mostrar información de la veterinaria
print(veterinaria.obtener_informacion())

# Mostrar información de los animales
for animal in veterinaria.get_animales():
    print(animal.obtener_informacion())

# Mostrar información de los clientes
for cliente in veterinaria.get_clientes():
    print(cliente.obtener_informacion())

# Mostrar información de los empleados
for empleado in veterinaria.get_empleados():
    print(empleado.obtener_informacion())

# Mostrar información de los servicios
for servicio in veterinaria.get_servicios():
    print(servicio.obtener_informacion())

# Mostrar información de las citas
for cita in veterinaria.get_citas():
    print(cita.obtener_informacion())
