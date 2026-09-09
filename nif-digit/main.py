def run(nif: str) -> str:
    # TODO
    dni = nif[:-1]
    letra = nif[-1].upper()
    letras = "TRWAGMYFPDXBNJZSQVHLCKE"
    index = int(dni) % 23
    wnif = dni + letras[index]
    
    return wnif


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
