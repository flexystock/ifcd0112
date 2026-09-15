def getint():

    valor_entrada = None
    while True:
        valor_entrada = int(input("Dame un valor entero"))
        try:
            int(valor_entrada)
        except ValueError:
            print("El valor no es un valor entero, introduzclo de nuevo")

        else:
            break

    return valor_entrada


# DO NOT TOUCH THE CODE BELOW
if __name__ == "__main__":
    import vendor

    vendor.launch(getint)
