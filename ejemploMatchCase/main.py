nota1 = int(input("Ingrese primer nota:"))
nota2 = int(input("Ingrese segunda nota:"))
nota3 = int(input("Ingrese tercer nota:"))
prom = (nota1 + nota2 + nota3) / 3

match prom:
    case n if n >= 7:
        print("Promocionado")
    case n if n >= 4:
        print("Regular")
    case _:
        print("Reprobado")