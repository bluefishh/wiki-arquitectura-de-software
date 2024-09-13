
class FiltroEliminarNegativos():
    def aplicar(self, datos):
        print("Eliminando los números negativos...")
        return [num for num in datos if num >= 0]

class FiltroEliminarDuplicados():
    def aplicar(self, datos):
        print("Eliminando los números duplicados...")
        return list(set(datos))

class FiltroOrdenar():
    def aplicar(self, datos):
        print("Ordenando los números...")
        return sorted(datos)

class ProcesadorNumeros:
    def __init__(self):
        self.filtros = []

    def agregar_filtro(self, filtro):
        self.filtros.append(filtro)

    def procesar(self, datos):
        resultado = datos
        for filtro in self.filtros:
            resultado = filtro.aplicar(resultado)
        return resultado
        
numeros = [5, -2, 10, 3, 5, -8, 10, 3]

procesador = ProcesadorNumeros()
print("Lista para procesar: ", numeros)
procesador.agregar_filtro(FiltroEliminarNegativos())
procesador.agregar_filtro(FiltroEliminarDuplicados())
procesador.agregar_filtro(FiltroOrdenar())

numeros_limpiados = procesador.procesar(numeros)
print("Resultado: ", numeros_limpiados)