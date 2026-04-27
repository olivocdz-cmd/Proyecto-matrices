def ingresar_matriz(filas_requeridas=None, columnas_requeridas=None):
    # --- 1. Validar las dimensiones ---
    while True:
        try:
            filas = int(input("Ingrese el número de filas: "))
            if filas_requeridas is not None and filas != filas_requeridas:
                print(f"Error: La operación requiere exactamente {filas_requeridas} fila(s).")
                continue # Vuelve al inicio del bucle para preguntar de nuevo

            columnas = int(input("Ingrese el número de columnas: "))
            if columnas_requeridas is not None and columnas != columnas_requeridas:
                print(f"Error: La operación requiere exactamente {columnas_requeridas} columna(s).")
                continue

            break # Si pasamos las validaciones, rompemos este bucle

        except ValueError:
            print("Error: Debe ingresar un número entero válido para las dimensiones.")

    # --- 2. Validar y capturar los elementos ---
    matriz = []
    for i in range(filas):
        while True:
            try:
                entrada_fila = input(f"Ingrese la fila {i + 1} separada por espacios: ")

                # Convertimos los textos ingresados a una lista de números (floats)
                fila_numeros = [float(x) for x in entrada_fila.split()]

                if len(fila_numeros) != columnas:
                    print(f"Error: Debe ingresar exactamente {columnas} valores.")
                else:
                    matriz.append(fila_numeros)
                    break # Fila ingresada correctamente, pasamos a la siguiente

            except ValueError:
                # Esto captura si el usuario escribe "a b c" en lugar de "1 2 3"
                print("Error: Asegúrese de ingresar solo números separados por espacios.")

    return matriz

def mostrar_matriz(matriz):
    print("Resultado:")
    for fila in matriz:
        # Formateamos para que se vea ordenado al imprimir
        print(" ".join(str(elemento) for elemento in fila))
    print() # Espacio extra al final
