class Veterinaria:
    def __init__(self, nombre, direccion, telefono, animales, clientes, empleados, citas, servicios):
        self._nombre = nombre
        self._direccion = direccion
        self._telefono = telefono
        self._animales = animales
        self._clientes = clientes
        self._empleados = empleados
        self._citas = citas
        self._servicios = servicios

    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_direccion(self):
        return self._direccion

    def set_direccion(self, direccion):
        self._direccion = direccion

    def get_telefono(self):
        return self._telefono

    def set_telefono(self, telefono):
        self._telefono = telefono

    def get_animales(self):
        return self._animales

    def set_animales(self, animales):
        self._animales = animales

    def get_clientes(self):
        return self._clientes

    def set_clientes(self, clientes):
        self._clientes = clientes

    def get_empleados(self):
        return self._empleados

    def set_empleados(self, empleados):
        self._empleados = empleados

    def get_citas(self):
        return self._citas

    def set_citas(self, citas):
        self._citas = citas

    def get_servicios(self):
        return self._servicios

    def set_servicios(self, servicios):
        self._servicios = servicios

    def obtener_informacion(self):
        return (f"Nombre: {self._nombre}, Dirección: {self._direccion}, Teléfono: {self._telefono}, "
                f"Animales: {self._animales}, Clientes: {self._clientes}, Empleados: {self._empleados}, "
                f"Citas: {self._citas}, Servicios: {self._servicios}")


class Animal:
    def __init__(self, nombre, raza, edad, dueño):
        self._nombre = nombre
        self._raza = raza
        self._edad = edad
        self._dueño = dueño

    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_raza(self):
        return self._raza

    def set_raza(self, raza):
        self._raza = raza

    def get_edad(self):
        return self._edad

    def set_edad(self, edad):
        self._edad = edad

    def get_dueño(self):
        return self._dueño

    def set_dueño(self, dueño):
        self._dueño = dueño

    def obtener_informacion(self):
        return (f"Nombre: {self._nombre}, Raza: {self._raza}, Edad: {self._edad}, Dueño: {self._dueño}")


class Cliente:
    def __init__(self, nombre, direccion, telefono):
        self._nombre = nombre
        self._direccion = direccion
        self._telefono = telefono

    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_direccion(self):
        return self._direccion

    def set_direccion(self, direccion):
        self._direccion = direccion

    def get_telefono(self):
        return self._telefono

    def set_telefono(self, telefono):
        self._telefono = telefono

    def obtener_informacion(self):
        return (f"Nombre: {self._nombre}, Dirección: {self._direccion}, Teléfono: {self._telefono}")


class Servicio:
    def __init__(self, tipo, costo):
        self._tipo = tipo
        self._costo = costo

    def get_tipo(self):
        return self._tipo

    def set_tipo(self, tipo):
        self._tipo = tipo

    def get_costo(self):
        return self._costo

    def set_costo(self, costo):
        self._costo = costo

    def obtener_informacion(self):
        return (f"Tipo: {self._tipo}, Costo: {self._costo}")


class Cita:
    def __init__(self, fecha, hora, animal, cliente, servicio):
        self._fecha = fecha
        self._hora = hora
        self._animal = animal
        self._cliente = cliente
        self._servicio = servicio

    def get_fecha(self):
        return self._fecha

    def set_fecha(self, fecha):
        self._fecha = fecha

    def get_hora(self):
        return self._hora

    def set_hora(self, hora):
        self._hora = hora

    def get_animal(self):
        return self._animal

    def set_animal(self, animal):
        self._animal = animal

    def get_cliente(self):
        return self._cliente

    def set_cliente(self, cliente):
        self._cliente = cliente

    def get_servicio(self):
        return self._servicio

    def set_servicio(self, servicio):
        self._servicio = servicio

    def obtener_informacion(self):
        return (f"Fecha: {self._fecha}, Hora: {self._hora}, Animal: {self._animal}, Cliente: {self._cliente}, "
                f"Servicio: {self._servicio}")


class Empleado:
    def __init__(self, nombre, puesto, salario):
        self._nombre = nombre
        self._puesto = puesto
        self._salario = salario

    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_puesto(self):
        return self._puesto

    def set_puesto(self, puesto):
        self._puesto = puesto

    def get_salario(self):
        return self._salario

    def set_salario(self, salario):
        self._salario = salario

    def obtener_informacion(self):
        return (f"Nombre: {self._nombre}, Puesto: {self._puesto}, Salario: {self._salario}")
