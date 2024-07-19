def main():
    stock = [0, 0, 0, 0, 0]
    no_hay_alertas = 0
    salida = 6
    cuatro = 4

    while True:
        print(".:: GESTIÓN DE INVENTARIO EMPRESA CONSTRUCTORA ::.")
        print(" ")
        print("1. Agregar material al inventario")
        print("2. Retirar material del inventario")
        print("3. Mostrar inventario")
        print("4. Mostrar alertas de inventario bajo")
        print("5. Actualizar inventario de todos los materiales")
        print("6. Salir")
        opc = int(input("Ingrese una opción: "))

        if opc == 1:
            print("Seleccione el material a agregar:")
            print("1. Cemento (bultos)")
            print("2. Arena (m3)")
            print("3. Grava (m3)")
            print("4. Ladrillos (unidades)")
            opcion_material = int(input())

            if 1 <= opcion_material <= 4:
                cantidad = int(input("Ingrese la cantidad a agregar: "))

                if opcion_material == 1:
                    stock[1] += cantidad
                elif opcion_material == 2:
                    stock[2] += cantidad
                elif opcion_material == 3:
                    stock[3] += cantidad
                elif opcion_material == 4:
                    stock[4] += cantidad

                print("Material agregado. Pulse una tecla para regresar al menú.")
                input()

        elif opc == 2:
            print("Seleccione el material a retirar:")
            print("1. Cemento")
            print("2. Arena")
            print("3. Grava")
            print("4. Ladrillos")
            opcion_material = int(input())

            if 1 <= opcion_material <= 4:
                cantidad = int(input("Ingrese la cantidad a retirar: "))

                if opcion_material == 1:
                    if stock[1] >= cantidad:
                        stock[1] -= cantidad
                        print("Material retirado, ingrese una tecla para continuar...")
                    else:
                        print("No hay suficiente cemento en el inventario, ingrese una tecla para continuar...")
                elif opcion_material == 2:
                    if stock[2] >= cantidad:
                        stock[2] -= cantidad
                        print("Material retirado, ingrese una tecla para continuar...")
                    else:
                        print("No hay suficiente arena en el inventario, ingrese una tecla para continuar...")
                elif opcion_material == 3:
                    if stock[3] >= cantidad:
                        stock[3] -= cantidad
                        print("Material retirado, ingrese una tecla para continuar...")
                    else:
                        print("No hay suficiente grava en el inventario, ingrese una tecla para continuar...")
                elif opcion_material == 4:
                    if stock[4] >= cantidad:
                        stock[4] -= cantidad
                        print("Material retirado, ingrese una tecla para continuar...")
                    else:
                        print("No hay suficientes ladrillos en el inventario, ingrese una tecla para continuar...")

                input()

        elif opc == 3:
            print("Inventario actual:")
            print(f"Cemento: {stock[1]}")
            print(f"Arena: {stock[2]}")
            print(f"Grava: {stock[3]}")
            print(f"Ladrillos: {stock[4]}")
            input("Ingrese una tecla para continuar...")

        elif opc == 4:
            no_hay_alertas = 0
            if stock[1] < 50:
                print("Alerta: Inventario de cemento bajo")
            else:
                no_hay_alertas += 1
            if stock[2] < 100:
                print("Alerta: Inventario de arena bajo")
            else:
                no_hay_alertas += 1
            if stock[3] < 75:
                print("Alerta: Inventario de grava bajo")
            else:
                no_hay_alertas += 1
            if stock[4] < 200:
                print("Alerta: Inventario de ladrillos bajo")
            else:
                no_hay_alertas += 1

            if no_hay_alertas == cuatro:
                print("No hay alertas, pulse una tecla para continuar...")
            else:
                print("Ingrese una tecla para continuar...")
            input()

        elif opc == 5:
            actualizar_inventario = True
            while actualizar_inventario:
                print("Actualizar inventario de Cemento:")
                cantidad = int(input("Ingrese la nueva cantidad: "))
                stock[1] += cantidad

                print("Actualizar inventario de Arena:")
                cantidad = int(input("Ingrese la nueva cantidad: "))
                stock[2] += cantidad

                print("Actualizar inventario de Grava:")
                cantidad = int(input("Ingrese la nueva cantidad: "))
                stock[3] += cantidad

                print("Actualizar inventario de Ladrillos:")
                cantidad = int(input("Ingrese la nueva cantidad: "))
                stock[4] += cantidad

                opcion_act = input("¿Desea continuar actualizando el inventario? (Si/No): ").strip().lower()
                if opcion_act != "si":
                    actualizar_inventario = False
                    input("Ingrese una tecla para continuar...")

        elif opc == 6:
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida, pulse para continuar...")
            input()

if __name__ == "__main__":
    main()
