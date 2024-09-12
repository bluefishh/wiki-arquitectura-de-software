class TareasControlador:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

    def agregar_tarea(self):
        tarea = self.vista.obtener_nueva_tarea()
        self.modelo.agregar_tarea(tarea)
        self.vista.mostrar_tareas(self.modelo.obtener_tareas())

    def mostrar_tareas(self):
        self.vista.mostrar_tareas(self.modelo.obtener_tareas())
