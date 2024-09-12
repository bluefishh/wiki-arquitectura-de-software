class TareasModelo:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)

    def obtener_tareas(self):
        return self.tareas