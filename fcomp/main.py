def run(xmin: int, xmax: int) -> list:

    """Utilizando listas por comprensi´on, crea una lista que contenga el resultado de aplicar la
       funci´on f(x) = 3x +2 para el rango de x dado en los valores de entrada."""

    #construir una lista con los valores de entrada
    inicio = xmin
    fin = xmax

    lista = list(range(inicio, fin + 1))

    #con esa lista, aplicar listas por compresion
    #SE PODRIA HACER TODO EN LA MISMA LINEA, PERO POR COMPRANSION LO HACEMOS 2
    values = [3 * x + 2 for x in lista]

    return values


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
