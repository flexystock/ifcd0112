def factorial(x: int):
    # Validamos que el argumento sea un número entero y que no sea un número negativo.
    # Si no cumple con esto, devolvemos None.
    if not isinstance(x, int) or x < 0:
        return None

    # Caso base: el factorial de 0 es 1 por definición matemática.
    elif x == 0:
        return 1

    # Caso recursivo: multiplicamos el número actual por el factorial del número anterior (x - 1).
    else:
        return x * factorial(x - 1)


# DO NOT TOUCH THE CODE BELOW
if __name__ == "__main__":
    import vendor

    vendor.launch(factorial)
