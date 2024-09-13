class CambiarClima:
    def __init__(self):
        self._observadores = []
        self._temperatura = 0

    def agregar_observador(self, observador):
        self._observadores.append(observador)

    def eliminar_observador(self, observador):
        self._observadores.remove(observador)

    def notificar_observadores(self):
        for observador in self._observadores:
            observador.actualizar(self._temperatura)

    def establecer_temperatura(self, nueva_temperatura):
        print(f"Clima: Nueva temperatura registrada para actualizar en los observadores: {nueva_temperatura}°C")
        self._temperatura = nueva_temperatura
        self.notificar_observadores()

class DispositivoObservadorUno():
    def actualizar(self, temperatura):
        print(f"Dispositivo 1: Temperatura actualizada a {temperatura}°C")

class DispositivoObservadorDos():
    def actualizar(self, temperatura):
        print(f"Dispositivo 2: Temperatura actualizada a {temperatura}°C")

clima = CambiarClima()

disp1 = DispositivoObservadorUno()
disp2 = DispositivoObservadorDos()

clima.agregar_observador(disp1)
clima.agregar_observador(disp2)

clima.establecer_temperatura(25)
clima.establecer_temperatura(30)