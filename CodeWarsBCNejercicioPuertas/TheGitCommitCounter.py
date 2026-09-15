while True:
    try:
        numero = int(input("Introduce un número entero entre '0' y '99': "))
        if 0 <= numero <= 99:
            break
        print("El número debe estar entre 0 y 99.")
    except ValueError:
        print("Error: Debes introducir un número entero válido.")
if numero == 1:
    print(f"Hace {numero} minuto")
else:
    print(f"Hace {numero} minutos")
