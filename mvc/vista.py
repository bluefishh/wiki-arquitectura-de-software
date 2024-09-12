class TareasVista:
    def mostrar_tareas(self, tareas):
        print("Lista de Tareas:")
        for i, tarea in enumerate(tareas, 1):
            print(f"{i}. {tarea}")
        if not tareas:
            print("No hay tareas.")

    def obtener_nueva_tarea(self):
        return input("Ingresa una nueva tarea: ")