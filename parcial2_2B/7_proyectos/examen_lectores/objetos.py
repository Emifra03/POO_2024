from clases import*

estudiante1 =Estudiantes("Ana Torres Guzman", "Col.centro 1500 ote", 618123456, "Meca", 2335678)
docente1 = Docentes("Daniel Fuentes Loera", "Fracc.D.Arrieta 1400 nte", 6183335678, "TI", 123)

print(f"Nombre del estudiante: {estudiante1.getNombre()}, Carrera: {estudiante1.getCarrera()}, Matrícula: {estudiante1.getMatricula()}")
print(f"Nombre del docente: {docente1.getNombre()}, Modalidad: {docente1.getModalidad()}, Número de Empleado: {docente1.getNumEmpleado()}")

estudiante1.reserva("Libro de Matemáticas")
estudiante1.entregar("Libro de Matemáticas")

docente1.reserva("Proyector")
docente1.entregar("Proyector")