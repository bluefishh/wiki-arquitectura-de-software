from esclavos import EsclavoMayusculas, EsclavoMinusculas, EsclavoContarPalabras

class Maestro:
    def __init__(self):
        self.esclavo_mayusculas = EsclavoMayusculas()
        self.esclavo_minusculas = EsclavoMinusculas()
        self.esclavo_contar_palabras = EsclavoContarPalabras()

    def procesar_texto(self, texto):
        resultado_mayusculas = self.esclavo_mayusculas.procesar(texto)
        resultado_minusculas = self.esclavo_minusculas.procesar(texto)
        resultado_contar_palabras = self.esclavo_contar_palabras.procesar(texto)
        
        print("Resultado en mayúsculas:", resultado_mayusculas)
        print("Resultado en minúsculas:", resultado_minusculas)
        print(f"Número de palabras: {resultado_contar_palabras}")
