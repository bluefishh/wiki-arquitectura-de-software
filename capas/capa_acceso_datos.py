from capa_base_de_datos import BaseDatosSimulada

class RepositorioHistorial:
    def __init__(self):
        self.base_datos = BaseDatosSimulada()

    def agregar_operacion(self, operacion):
        self.base_datos.insertar_operacion(operacion)

    def obtener_historial(self):
        return self.base_datos.obtener_historial()
