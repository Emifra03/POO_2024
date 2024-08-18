import os
def borrar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def esperar_tecla():
    input("\nPresiona Enter para continuar...")
