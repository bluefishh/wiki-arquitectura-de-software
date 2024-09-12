class BaseDatosSimulada:
    def __init__(self):
        self.historial = []

    def insertar_operacion(self, operacion):
        self.historial.append(operacion)

    def obtener_historial(self):
        return self.historial
