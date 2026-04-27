def ingresar_matriz(filas_requeridas=None, columnas_requeridas=None):
    while True:
        try:
            filas = int(input("Ingrese el número de filas: "))
            if filas_requeridas is not None and filas != filas_requeridas:
                print(f"Error: La operación requiere exactamente {filas_requeridas} fila(s).")
                continue

            columnas = int(input("Ingrese el número de columnas: "))
            if columnas_requeridas is not None and columnas != columnas_requeridas:
                print(f"Error: La operación requiere exactamente {columnas_requeridas} columna(s).")
                continue

            break

        except ValueError:
            print("Error: Debe ingresar un número entero válido para las dimensiones.")

    matriz = []
    for i in range(filas):
        while True:
            try:
                entrada_fila = input(f"Ingrese la fila {i + 1} separada por espacios: ")

                fila_numeros = [float(x) for x in entrada_fila.split()]

                if len(fila_numeros) != columnas:
                    print(f"Error: Debe ingresar exactamente {columnas} valores.")
                else:
                    matriz.append(fila_numeros)
                    break

            except ValueError:
                print("Error: Asegúrese de ingresar solo números separados por espacios.")

    return matriz

def mostrar_matriz(matriz):
    print("Resultado:")
    for fila in matriz:
        print(" ".join(str(elemento) for elemento in fila))
    print()