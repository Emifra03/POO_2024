nombre_trabajador = "nombre"
horas_trabajadas = "horas"
dias_trabajados = "dias"
sueldo_hora = "sueldo"

contador= 1
while contador<= 5 :
   print(input("ingresa el nombre del trabajador :"))
   print(input("ingresa las horas trabajadas :")) 
   print(input("ingresa los dias trabajados :"))
   print(input("ingresa el sueldo :"))
contador+= 1

sueldo_total =  horas_trabajadas * sueldo_hora * dias_trabajados
sueldo_mes = sueldo_total * 5

print (input("¿Desea ingresar nuevos datos? (si/no)"))


