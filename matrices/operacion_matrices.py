def suma_matrices(A, B):
    if not A or not B or len(A) != len(B) or len(A[0]) != len(B[0]):
        return "Error: Las matrices deben tener las mismas dimensiones."
    resultado = []
    for i in range(len(A)):
        fila = []
        for j in range(len(A[0])):
            fila.append(A[i][j] + B[i][j])
        resultado.append(fila)
    return resultado

def multiplicacion_matrices(A, B):
    if not A or not B or len(A[0]) != len(B):
        return "Error: Columnas de A deben coincidir con filas de B."
    resultado = []
    for i in range(len(A)):
        fila = []
        for j in range(len(B[0])):
            suma = 0
            for k in range(len(A[0])):
                suma += A[i][k] * B[k][j]
            fila.append(suma)
        resultado.append(fila)
    return resultado

def producto_hadamard(A, B):
    if not A or not B or len(A) != len(B) or len(A[0]) != len(B[0]):
        return "Error: Las matrices deben tener las mismas dimensiones."
    resultado = []
    for i in range(len(A)):
        fila = []
        for j in range(len(A[0])):
            fila.append(A[i][j] * B[i][j])
        resultado.append(fila)
    return resultado

def producto_kronecker(A, B):
    resultado = []
    for fila_A in A:
        for fila_B in B:
            nueva_fila = []
            for elem_A in fila_A:
                for elem_B in fila_B:
                    nueva_fila.append(elem_A * elem_B)
            resultado.append(nueva_fila)
    return resultado