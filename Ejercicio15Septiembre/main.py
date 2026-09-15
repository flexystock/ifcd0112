"""
Hacer una clase que mantenga un agregado de polígonos regulares. Los polígonos pueden ser al menos: triángulos, cuadrados, rectángulos, pentágonos y círculos.
Para cada polígono se ha de guardar el número de lados o su radio y los datos necesarios para calcular el área y el perímetro.
Ha de tener un método que calcule el área y otro para el perímetro.
Implementar dos objetos de la clase y añadirle a cada uno de ellos 3 polígonos.
Mostrar para cada agregado: el tipo de polígono , su perímetro y área."""

import math


class Poligono:
    def __init__(self, listado: list | None = None):
        self.__listado = listado if listado is not None else []

    def set_poligono(self, tipo_figura):
        self.__listado.append(tipo_figura)

    def get_poligono(self):

        # Recorremos toda la lista de los polígonos guardados en __listado
        for figura in self.__listado:
            tipo = figura.__class__.__name__
            area = figura.calcula_area()
            perimetro = figura.calcula_perimetro()
            print(f"   - Tipo: {tipo} | Perímetro: {perimetro:.2f} | Área: {area:.2f}")

    def CalculaArea(self):
        pass

    def CalcularPerimetro(self):
        pass


class Triangulo(Poligono):
    def __init__(self, lados: int, medida: float):
        super().__init__()
        self.__lados = lados
        self.__medida = medida

    def calcula_area(self):
        return (math.sqrt(3) / 4) * (self.__medida**2)

    # Cambiado a minúsculas para que coincida con los demás
    def calcula_perimetro(self):
        return self.__lados * self.__medida


class Cuadrado(Poligono):
    def __init__(self, lados: int, medida: float):
        # llamamos/iniciamos a la clase padre
        super().__init__()
        self.__lados = lados
        self.__medida = medida

    # METODO PARA CALCULAR EL AREA -> lado al cuadrado
    def calcula_area(self):
        return self.__medida**2

    # METODO PARA CALCULAR EL PERIMETO -> medida * 4
    def calcula_perimetro(self):
        return self.__lados * self.__medida


class Rectangulo(Poligono):
    def __init__(self, lados: int, medida_lado_1: float, medida_lado_2: float):
        super().__init__()
        self.__lados = lados
        self.__medida_lado_1 = medida_lado_1
        self.__medida_lado_2 = medida_lado_2

    # METODO PARA CALCULAR EL AREA (lado * lado)
    def calcula_area(self):
        return self.__medida_lado_1 * self.__medida_lado_2

    # METODO PARA CALCULAR EL PERIMETO (sume de los lados)
    def calcula_perimetro(self):
        return 2 * (self.__medida_lado_1 + self.__medida_lado_2)


class Pentagono(Poligono):
    def __init__(self, lados: int, medida_lado: float):
        super().__init__()
        self.__lados = lados
        self.__medida_lado = medida_lado

    # METODO PARA CALCULAR EL AREA
    def calcula_area(self):
        perimetro = self.calcula_perimetro()
        apotema = self.__medida_lado / (2 * math.tan(math.pi / 5))
        return (perimetro * apotema) / 2

    # METODO PARA CALCULAR EL PERIMETO
    def calcula_perimetro(self):
        return self.__lados * self.__medida_lado


class Circulo(Poligono):
    def __init__(self, radio: float):
        super().__init__()
        self.__radio = radio

    # METODO PARA CALCULAR EL AREA: pi * radio ** 2
    def calcula_area(self):
        return math.pi * (self.__radio**2)

    # METODO PARA CALCULAR EL PERIMETO 2*pi*radio
    def calcula_perimetro(self):
        return 2 * math.pi * self.__radio


agregado_1 = Poligono()
agregado_1.set_poligono(Triangulo(3, 5.0))
agregado_1.set_poligono(Cuadrado(4, 4.0))
agregado_1.set_poligono(Circulo(3.0))

# Creamos el Agregado 2
agregado_2 = Poligono()
agregado_2.set_poligono(Rectangulo(4, 3.0, 6.0))
agregado_2.set_poligono(Pentagono(5, 4.0))
agregado_2.set_poligono(Cuadrado(4, 6.0))

print("--- Datos del Agregado 1 ---")
agregado_1.get_poligono()

print("\n--- Datos del Agregado 2 ---")
agregado_2.get_poligono()
