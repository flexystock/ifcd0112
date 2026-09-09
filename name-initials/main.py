def run(fullname: str) -> str:

    # Primero obtenemos con .split los elemntos de la lista (separados por , segun el enunciado)
    #  ejemplo -> 'apellido, nombre'

    apellidos_nombre = fullname.split(",")

    # tendriamos la siguiente lista -> [apellidos, nombre]

    # separamos los apellidos -> [apellido1, apellido2]
    # no ponemos delimitador por venir directamente del ejemplo sin él

    apellidos = apellidos_nombre[0].split()

    # obteniendo lo siguiente: en apellidos_nombre[1] -> Nombre
    # obteniendo lo siguiente: en apellidos_nombre[0][0] -> Primer apellido
    # obteniendo lo siguiente: en apellidos_nombre[0][1] -> Segundo apellido
    inicial_nombre = apellidos_nombre[1].strip()[0].upper() + "."
    inicial_apellidos = (
        apellidos[0][0].upper() + "." + (apellidos[1][0].upper() + ".")
        if len(apellidos) > 1
        else apellidos[0][0].upper() + "."
    )

    return inicial_nombre + inicial_apellidos


# DO NOT TOUCH THE CODE BELOW
if __name__ == "__main__":
    import vendor

    vendor.launch(run)
