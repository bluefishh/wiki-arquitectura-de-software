class ServicioCalculadora:
    def __init__(self, repositorio):
        self.repositorio = repositorio

    def sumar(self, a, b):
        resultado = a + b
        self.repositorio.agregar_operacion(f"{a} + {b} = {resultado}")
        return resultado

    def restar(self, a, b):
        resultado = a - b
        self.repositorio.agregar_operacion(f"{a} - {b} = {resultado}")
        return resultado

    def multiplicar(self, a, b):
        resultado = a * b
        self.repositorio.agregar_operacion(f"{a} * {b} = {resultado}")
        return resultado

    def dividir(self, a, b):
        if b == 0:
            raise ValueError("No se puede dividir por cero.")
        resultado = a / b
        self.repositorio.agregar_operacion(f"{a} / {b} = {resultado}")
        return resultado

    def obtener_historial(self):
        return self.repositorio.obtener_historial()
