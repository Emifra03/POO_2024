class Lectores:
    def _init_(self, nombre, direccion, tel):
        self.nombre  = nombre
        self.direccion = direccion
        self.tel = tel

    def getNombre(self):
        return self._nombre

    def setNombre(self, nombre: str):
        self._nombre = nombre

    def getDireccion(self):
        return self._direccion

    def setDireccion(self, direccion: str):
        self._direccion = direccion

    def getTelefono(self):
        return self._telefono

    def setTelefono(self, telefono: int):
        self._telefono = telefono

    def reserva(self, item: str):
        print(f"{self._nombre}  reservado {item}.")

    def entregar(self, item: str):
        print(f"{self._nombre} entregado {item}.")



class alumno(Lectores):
    def _init_(self, nombre: str, direccion: str, telefono: int, carrera: str, matricula: int):
        super()._init_(nombre, direccion, telefono)
        self._carrera = carrera
        self._matricula = matricula


    def getCarrera(self):
        return self._carrera

    def setCarrera(self, carrera: str):
        self._carrera = carrera

    def getMatricula(self):
        return self._matricula

    def setMatricula(self, matricula: int):
        self._matricula = matricula

    def reserva(self, item: str):
        super().reserva(item)
        print(f"Estudiante con matrícula {self._matricula} entrego {item}.")

    def entregar(self, item: str):
        super().entregar(item)
        print(f"Estudiante con matrícula {self._matricula} entrego {item}.")

    def getCarrera(self):
        return self._carrera

    def setCarrera(self, carrera: str):
        self._carrera = carrera

    def getMatricula(self):
        return self._matricula

    def setMatricula(self, matricula: int):
        self._matricula = matricula

    def reserva(self, item: str):
        super().reserva(item)
        print(f"Estudiante con matrícula {self._matricula} reservo {item}.")

    def entregar(self, item: str):
        super().entregar(item)
        print(f"Estudiante con matrícula {self._matricula} reservo {item}.")


class Docentes(Lectores):
    def _init_(self, nombre: str, direccion: str, telefono: int, modalidad: str, num_empleado: int):

        super()._init_(nombre, direccion, telefono)
        self._modalidad = modalidad
        self._num_empleado = num_empleado
