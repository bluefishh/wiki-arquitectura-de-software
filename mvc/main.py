from modelo import TareasModelo
from vista import TareasVista
from controlador import TareasControlador

def main():
    modelo = TareasModelo()
    vista = TareasVista()
    controlador = TareasControlador(modelo, vista)

    while True:
        print("\n1. Agregar Tarea")
        print("2. Ver Tareas")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            controlador.agregar_tarea()
        elif opcion == '2':
            controlador.mostrar_tareas()
        elif opcion == '3':
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()