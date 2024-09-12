from capa_acceso_datos import RepositorioHistorial
from capa_log_negocio import ServicioCalculadora

def main():
    repositorio = RepositorioHistorial()
    calculadora = ServicioCalculadora(repositorio)

    while True:
        print("\n1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Ver historial")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion in ['1', '2', '3', '4']:
            a = int(input("Ingrese el primer número: "))
            b = int(input("Ingrese el segundo número: "))
            
            if opcion == '1':
                print(f"Resultado: {calculadora.sumar(a, b)}")
            elif opcion == '2':
                print(f"Resultado: {calculadora.restar(a, b)}")
            elif opcion == '3':
                print(f"Resultado: {calculadora.multiplicar(a, b)}")
            elif opcion == '4':
                try:
                    print(f"Resultado: {calculadora.dividir(a, b)}")
                except ValueError as e:
                    print(f"Error: {e}")
        elif opcion == '5':
            historial = calculadora.obtener_historial()
            print("Historial de operaciones:")
            for operacion in historial:
                print(operacion)
        elif opcion == '6':
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()