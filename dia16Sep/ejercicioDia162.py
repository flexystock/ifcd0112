"""Crear una clase Fabrica que tenga los atributos de Llantas, Color y Precio;
luego crear dos clases más que hereden de Fabrica, las cuales son Moto y Carro.
Crear métodos que muestren la cantidad de llantas, color y precio de ambos transportes.
Por último, crear objetos para cada clase y mostrar por pantalla los atributos de cada uno."""


class Fabrica:
    def __init__(self, llantas: int, color: str, precio: float):
        self.__llantas = llantas
        self.__color = color
        self.__precio = precio
        self.__especializacion = {"1": "Llantas", "2": "Color"}

    def get_llantas(self):
        return self.__llantas

    def get_color(self):
        return self.__color

    def get_precio(self):
        return self.__precio


class Carro(Fabrica):
    def __init__(self, color: str, precio: float):
        # Un carro siempre tiene 4 llantas por defecto
        super().__init__(4, color, precio)

    def __str__(self):
        return f"Carro -> Llantas: {self.get_llantas()}, Color: {self.get_color()}, Precio: {self.get_precio()} €"


class Moto(Fabrica):
    def __init__(self, color: str, precio: float):
        # Una moto siempre tiene 2 llantas por defecto
        super().__init__(2, color, precio)

    def __str__(self):
        return f"Moto -> Llantas: {self.get_llantas()}, Color: {self.get_color()}, Precio: {self.get_precio()} €"


if __name__ in ("__main__", "ejercicioDia162"):
    # Creamos objetos para cada clase
    mi_carro = Carro("Rojo", 18500.50)
    mi_moto = Moto("Negra", 5200.00)

    # Mostramos por pantalla los atributos
    print(mi_carro)
    print(mi_moto)
