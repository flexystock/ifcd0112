def run(A: list, B: list) -> list:
    """Matriz  A x Matriz B:  6 4     3 2  = 6·3+4·1   6·2+4·7 = 22 40
                              8 9  x  1 7  = 8·3+9·1   8·2+9·7 = 33 79
    """
    """En python
       filas X columnas 
       lista A [[6,4],[8,9]]
       lista B [[3,2],[1,7]] """

      # Calculamos cada uno de los 4 elementos resultantes usando los índices
    c00 = A[0][0] * B[0][0] + A[0][1] * B[1][0]
    c01 = A[0][0] * B[0][1] + A[0][1] * B[1][1]
    c10 = A[1][0] * B[0][0] + A[1][1] * B[1][0]
    c11 = A[1][0] * B[0][1] + A[1][1] * B[1][1]
    
    # Estructuramos el resultado como una lista de listas (matriz 2x2)
    matriz_resultante = [
        [c00, c01],
        [c10, c11]
    ]
    
    return matriz_resultante



# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
