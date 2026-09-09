LETRAS = "TRWAGMYFPDXBNJZSQVHLCKE"

def letra_nif(dni: int) ->str:
    resto = dni % 23
    return LETRAS[resto]
print(letra_nif(53618727))
