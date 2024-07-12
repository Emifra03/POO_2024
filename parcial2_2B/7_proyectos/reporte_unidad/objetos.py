from clases import Cemento, Arena, Grava, Ladrillos

class Inventario:
    def __init__(self):
        self.cemento = Cemento()
        self.arena = Arena()
        self.grava = Grava()
        self.ladrillo = Ladrillos()
        self.no_hay_alertas = 0
        self.cuatro = 4
        self.salida = 6

    def limpiar_pantalla(self):
        print("\033c", end="")

    def esperar_tecla(self):
        input("Presiona una tecla para continuar...")

    def mostrar_menu(self):
        self.limpiar_pantalla()
        print(".:: GESTIÓN DE INVENTARIO EMPRESA CONSTRUCTORA ::.")
        print("1. Agregar material al inventario")
        print("2. Retirar material del inventario")
        print("3. Mostrar inventario")
        print("4. Mostrar alertas de inventario bajo")
        print("5. Actualizar inventario de todos los materiales")
        print("6. Salir")
        opc = int(input("Ingrese una opción: "))
        return opc

    def gestionar_inventario(self):
        while True:
            opc = self.mostrar_menu()
            if opc == 1:
                self.agregar_material()
            elif opc == 2:
                self.retirar_material()
            elif opc == 3:
                self.mostrar_inventario()
            elif opc == 4:
                self.mostrar_alertas()
            elif opc == 5:
                self.actualizar_inventario()
            elif opc == 6:
                print("Saliendo del programa...")
                break
            else:
                print("Opción inválida, pulse para continuar...")
                self.esperar_tecla()

    def agregar_material(self):
        self.limpiar_pantalla()
        print("Seleccione el material a agregar:")
        print("1. Cemento (bultos)")
        print("2. Arena (m3)")
        print("3. Grava (m3)")
        print("4. Ladrillos (unidades)")
        opcion_material = int(input())
        if 1 <= opcion_material <= 4:
            cantidad = int(input("Ingrese la cantidad a agregar: "))
            if opcion_material == 1:
                self.cemento.agregar(cantidad)
            elif opcion_material == 2:
                self.arena.agregar(cantidad)
            elif opcion_material == 3:
                self.grava.agregar(cantidad)
            elif opcion_material == 4:
                self.ladrillo.agregar(cantidad)
            print("Material agregado.")
            self.esperar_tecla()
        else:
            print("Opción inválida.")
            self.esperar_tecla()

    def retirar_material(self):
        self.limpiar_pantalla()
        print("Seleccione el material a retirar:")
        print("1. Cemento")
        print("2. Arena")
        print("3. Grava")
        print("4. Ladrillos")
        opcion_material = int(input())
        if 1 <= opcion_material <= 4:
            cantidad = int(input("Ingrese la cantidad a retirar: "))
            if opcion_material == 1:
                self.cemento.retirar(cantidad)
            elif opcion_material == 2:
                self.arena.retirar(cantidad)
            elif opcion_material == 3:
                self.grava.retirar(cantidad)
            elif opcion_material == 4:
                self.ladrillo.retirar(cantidad)
            self.esperar_tecla()
        else:
            print("Opción inválida.")
            self.esperar_tecla()

    def mostrar_inventario(self):
        self.limpiar_pantalla()
        print("Inventario actual:")
        print(self.cemento.mostrar())
        print(self.arena.mostrar())
        print(self.grava.mostrar())
        print(self.ladrillo.mostrar())
        self.esperar_tecla()

    def mostrar_alertas(self):
        self.limpiar_pantalla()
        self.no_hay_alertas = 0
        if self.cemento.get_cantidad() < 50:
            print("Alerta: Inventario de cemento bajo")
        else:
            self.no_hay_alertas += 1

        if self.arena.get_cantidad() < 100:
            print("Alerta: Inventario de arena bajo")
        else:
            self.no_hay_alertas += 1

        if self.grava.get_cantidad() < 75:
            print("Alerta: Inventario de grava bajo")
        else:
            self.no_hay_alertas += 1

        if self.ladrillo.get_cantidad() < 200:
            print("Alerta: Inventario de ladrillos bajo")
        else:
            self.no_hay_alertas += 1

        if self.no_hay_alertas == self.cuatro:
            print("No hay alertas.")
        self.esperar_tecla()

    def actualizar_inventario(self):
        while True:
            self.limpiar_pantalla()
            cantidad = int(input("Actualizar inventario de Cemento: Ingrese la nueva cantidad: "))
            self.cemento.set_cantidad(cantidad)
            cantidad = int(input("Actualizar inventario de Arena: Ingrese la nueva cantidad: "))
            self.arena.set_cantidad(cantidad)
            cantidad = int(input("Actualizar inventario de Grava: Ingrese la nueva cantidad: "))
            self.grava.set_cantidad(cantidad)
            cantidad = int(input("Actualizar inventario de Ladrillos: Ingrese la nueva cantidad: "))
            self.ladrillo.set_cantidad(cantidad)
            opcion_act = input("¿Desea continuar actualizando el inventario? (Si/No): ").lower()
            if opcion_act != 'si':
                break
        self.esperar_tecla()

if __name__ == "__main__":
    inventario = Inventario()
    inventario.gestionar_inventario()
