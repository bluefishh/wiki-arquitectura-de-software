class EsclavoMayusculas:
    def procesar(self, texto):
        return texto.upper()

class EsclavoMinusculas:
    def procesar(self, texto):
        return texto.lower()

class EsclavoContarPalabras:
    def procesar(self, texto):
        return len(texto.split())