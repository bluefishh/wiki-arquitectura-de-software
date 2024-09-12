from maestro import Maestro

def main():
    maestro = Maestro()

    while True:
        texto = input("Ingrese una cadena de texto (o escriba '1' para terminar): ")
        if texto == "1":
            break

        maestro.procesar_texto(texto)

if __name__ == "__main__":
    main()
