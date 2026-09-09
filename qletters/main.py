def run(letters: str) -> list[str]:
    cola = []

    for char in letters:
        if char == ' ':
            # El carácter policía limpia la cola actual
            cola.clear()
        else:
            cola.append(char)

    # Separar mayúsculas y minúsculas manteniendo el orden de llegada de cada grupo
    mayusculas = []
    for c in cola:
        if c.isupper():
            mayusculas.append(c)
    minusculas = []
    for c in cola:
            if c.islower():
                mayusculas.append(c)

    # Las mayúsculas van delante de las minúsculas
    return mayusculas + minusculas


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
