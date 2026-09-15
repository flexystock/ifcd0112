import random


class Cliente:
    # atributos
    __dni: str = ""
    __nombre: str = ""
    __apellidos: str = ""

    # metodos
    def __init__(self, dni, nombre, apellidos):
        self.__dni = dni
        self.__nombre = nombre
        self.__apellidos = apellidos

    def get_nombre(self):
        return self.__nombre

    def get_dni(self):
        return self.__dni

    def get_apellidos(self):
        return self.__apellidos


class Movimiento:
    # atributos
    __concepto: str
    __cantidad: float


class Cuenta:
    __numero: int
    __titular: Cliente
    __movimientos: list[Movimiento]

    def __init__(self, titular: Cliente):
        self.__titular = titular
        self.__numero = int("".join([str(random.randint(0, 9)) for _ in range(10)]))
        self.__saldo = 0

    def get_saldo(self):
        return self.__saldo

    def get_titular(self):
        return self.__titular

    def set_movimiento(self, movimiento):
        self.__movimientos.append(movimiento)

    def get_numero(self):
        return self.__numero


# definimos una lista de clientes
clientes = []
clientes.append(Cliente("1234567T", "PepedElDESA", "Rivera"))
clientes.append(Cliente("25698547T", "Juan", "ALvarez"))


# Creamos la cuenta de Pepe

cuentaDePepe = Cuenta(clientes[0])

print(
    f"El saldo de {cuentaDePepe.get_titular().get_nombre()} es de {cuentaDePepe.get_saldo()} €"
)
