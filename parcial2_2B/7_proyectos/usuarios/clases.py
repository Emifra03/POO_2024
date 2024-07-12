class usuarios:

 def __init__ (self,nombre,direccion,tel):
   self.nombre=nombre
   self.direccion= direccion 
   self.tel=tel


 def info_usuario(self):
    print(f"El usuario # {self.getNum_cliente()} es el cliente: {self.getNombre()} y la direccion es: {self.getDireccion()} y el telefono es: {self.getTel()}")


    def getNombre(self):
        return self.nombre

    def getDireccion(self):
        return self.direccion

    def getTel(self):
        return self.tel             

    def setNombre(self,nombre):
        self.nombre=nombre

    def setDireccion(self,direccion):
        self.direccion=direccion

    def setTel(self,tel):
        self.tel=tel



class Clientes(usuarios):
   def __init__(self,nombre,direccion,tel,num_cliente,tipo,salario):
      super().__init__(nombre,direccion,tel)
      self._salario=salario
      self.__num_cliente=num_cliente

   def info_usuario(self):
     print(f"el usuario es # {self.getNum_cliente()} es el cliente:{self.getNombre()} y la direccion es:{self.getDireccion()} y el telefono es:{self.getTel()},tiene un salario de:{self.getSalario()} ")

   def getNum_empleado(self):
      return self._num_empleado

   def setNum_empleado(self,num_empleado):
       self._num_empleado=num_empleado       
  
   def getSalario(self):
      return self._salario

   def setSalario(self,salario):
       self._salario=salario

   def getTipo(self):
      return self._tipo

   def setTipo(self,tipo):
      self._tipo=tipo