class Material:
    def __init__(self, nombre, cantidad=0):
        self._nombre = nombre
        self._cantidad = cantidad

    def agregar(self, cantidad):
        self._cantidad += cantidad

    def retirar(self, cantidad):
        if self._cantidad >= cantidad:
            self._cantidad -= cantidad
            return True
        else:
            print(f"No hay suficiente {self._nombre} en el inventario")
            return False

    def mostrar(self):
        return f"{self._nombre}: {self._cantidad}"

    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_cantidad(self):
        return self._cantidad

    def set_cantidad(self, cantidad):
        self._cantidad = cantidad


class Cemento(Material):
    def __init__(self, cantidad=0):
        super().__init__('Cemento', cantidad)


class Arena(Material):
    def __init__(self, cantidad=0):
        super().__init__('Arena', cantidad)


class Grava(Material):
    def __init__(self, cantidad=0):
        super().__init__('Grava', cantidad)


class Ladrillos(Material):
    def __init__(self, cantidad=0):
        super().__init__('Ladrillo', cantidad)
