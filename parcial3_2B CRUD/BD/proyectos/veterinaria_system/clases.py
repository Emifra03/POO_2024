class veterinaria:

 def __init__(self,nombre, direccion, telefono, animal, clientes, empleados, citas, servicios ):
  self._nombre=nombre
  self._direccion=direccion
  self._telfono=telefono
  self._animal=animal
  self._clientes=clientes
  self._empleados=empleados
  self._citas=citas
  self._servicios=servicios

 def getNombre(self):
  return self._nombre
 
 def setNombre(self,nombre):
  self._nombre=nombre

 def getDireccion(self):
  return self._direccion
 
 def setDireccion(self,direccion):
  self._direccion=direccion

  def getTelefono(self):
   return self._telfono
 
 def setTelefono(self,telefono):
  self._telfono=telefono

  def getAnimales(self):
   return self._animales
  
  def setAnimales(self,animales):
   self._animales=animales

  def getClientes(self):
   return self._clientes
  
  def setClientes(self,clientes):
   self._clientes=clientes

  def getEmpleados(self):
   return self._empleados
  
  def setEmpleados(self,empleados):
   self._empleados=empleados

  def getCitas(self):
   return self._citas
  
  def setCitas(self,citas):
   self._citas=citas

  def getServicios(self):
   return self._servicios
  
  def setServicios(self,servicios):
   self._servicios=servicios
 def obtener_informacion(self):
  return (f"Nombre:{self._nombre()}, Direccion:{self._direccion()}, Telefono:{self._telefono()}, Animales{self._animales}")

class animal(veterinaria):
 def __init__(self, nombre, raza, edad, dueño):
  self._nombre=nombre
  self._raza=raza
  self._edad=edad
  self._dueño=dueño

  def getNombre(self):
   return self._nombre
 
 def setNombre(self,nombre):
  self._nombre=nombre

  def getRaza(self):
   return self.raza
 
 def setRaza(self,raza):
  self.raza=raza

 def getDueño(self):
  return self._dueño
 
 def setDueño(self,dueño):
  self._dueño=dueño
 def obtener_informacion(self):
  return (f"Nombre:{self._nombre()}, Raza:{self._raza()}, Edad:{self._edad()}, Dueño:{self._dueño()}")



class usuarios(veterinaria):
 def __init__(self,nombre,direccion,telefono):
  self._nombre=nombre
  self._direccion=direccion
  self._telfono=telefono

  def getNombre(self):
   return self._nombre
 
 def setNombre(self,nombre):
  self._nombre=nombre

 def getDireccion(self):
  return self._direccion
 
 def setDireccion(self,direccion):
  self._direccion=direccion

  def getTelefono(self):
   return self._telfono
 
 def setTelefono(self,telefono):
  self._telfono=telefono
 def obtener_informacion(self):
  return (f"Nombre:{self._nombre()}, Direccion:{self._direccion()}, Telefono:{self._telefono()}")

class servicio(veterinaria):
 def __init__(self, tipo, costo):
  super().__init__(tipo, costo)

  self._tipo=tipo
  self._costo=costo

  def getTipo(self):
   return self._tipo
 
 def setTipo(self,tipo):
  self._tipo=tipo

 def getCosto(self):
  return self._costo
 
 def setCosto(self,costo):
  self._costo=costo
 def obtener_informacion(self):
  return (f"Tipo:{self._tipo()}, Costo:{self._costo()}")

class cita(veterinaria):
 def __init__(self, fecha, hora, animal, cliente, servicio):
  super().__init__(fecha, hora, animal, cliente, servicio)

  self._fecha=fecha
  self._hora=hora
  self._animal=animal
  self._cliente=cliente
  self._servicio=servicio

  def getFecha(self):
   return self._fecha
 
 def setfecha(self,fecha):
  self._fecha=fecha

 def getHoras(self):
  return self._horas
 
 def setHoras(self,horas):
  self._horas=horas

  def getAnimal(self):
   return self.animal
 
 def setAnimal(self,animal):
  self.animal=animal

  def getCliente(self):
   return self._cliente
  
  def setCliente(self,cliente):
   self._cliente=cliente

  def getServicios(self):
   return self._servicios

  def setServicios(self,servicios):
   self._Servicios=servicios
 def obtener_informacion(self):
  return (f"Fecha:{self._fecha()}, Hora:{self._hora()}, Animal:{self._animal()}, Cliente:{self._cliente()}, Servicio:{self._servicio()}")

class empleado(veterinaria):
 def __init__(self, nombre, puesto,salario):
  super().__init__(nombre, puesto,salario)

  self._nombre=nombre
  self._puesto=puesto
  self._salario=salario

  def getNombre(self):
   return self.nombre
 
 def setNombre(self,nombre):
  self.nombre=nombre

  def getPuesto(self):
   return self._puesto
  
  def setPuesto(self,puesto):
   self._puesto=puesto

  def getPuesto(self):
   return self._puesto

  def setPuesto(self,puesto):
   self._puesto=puesto
  def obtener_informacion(self):
   return (f"Nombre:{self._nombre()}, Puesto:{self._puesto()}, Salario:{self._salario()}")

  

