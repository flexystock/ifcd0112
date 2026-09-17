"""
Desarrollar un script de python que permita gestionar la información requerida en el siguiente supuesto.
Durante el prototipado de vehículos, se requiere gestionar las piezas necesarias para su fabricación.
Los vehículos pueden ser del tipo: camión, autobús, automóvil o bicicleta.
Cada prototipo de vehículo se compone de:
un chasis adecuado para un tipo concreto vehículo y que tiene un número de identificación único.
un motor utilizado, si son motorizados. Interesa conocer su potencia y el combustible utilizado (ej. gasolina, gasoil, GLP, electricidad, …).
Hay que tener en cuenta que pueden surgir nuevos combustibles.
un número de ejes.
un número de ruedas. Cada tipo tiene un número de ruedas por defecto, aunque puede variar.
un número de asientos.
capacidad de carga. En el caso de los camiones interesa su TARA y peso máximo autorizado.
Los componentes son suministrados por diversas fábricas. Una fábrica puede suministrar uno o varios componentes.
Todas las fábricas tienen catalogados sus componentes como: chasis, motor, ruedas, asientos.
Las fabricas gestionan su propio stock de componentes y almacenan su precio de compra y precio de venta.
Es necesario poder localizar las fábricas que tienen componentes válidos para un determinado tipo de vehículo y conocer su stock.
Cada prototipo ha de almacenar la fábrica seleccionada para suministrar cada uno de sus componentes y el coste total de los mismos.
Para cada prototipo, se han de poder listar sus componentes mostrando el nombre del fabricante, el número de unidades requeridas, el precio unitario y el precio total.
Cada vez que se muestra esta información, se ha de generar un fichero que tenga por nombre el número del chasis y cuyo contenido sea igual al visualizado por pantalla.
Este fichero ha de estar siempre en su última versión.
Una vez configurado un prototipo, se requiere validar que las fábricas seleccionadas tienen suficiente número de componentes para llevar a cabo la fabricación de 100 vehículos.
Si alguna fábrica no tiene suficientes componentes, se ha de producir una excepción que muestre un mensaje indicando
que no se puede fabricar por faltar un determinado número de unidades de alguno de sus componentes."""

"""NOTA: cuando queramos fabricar un vehículo habra que darle unos datos minimos para la fabricacion (numero chasis, numero de reudas y numero de asientos)"""
from typing import ClassVar


class Vehiculo:
    # atributos:
    # se crean con el constructor
    def __init__(self, tipo_vehiculo, id_chasis, ejes, ruedas, asientos):
        self.tipo_vehiculo: str = tipo_vehiculo
        self.id_chasis: str = id_chasis
        self.ejes: int = ejes
        self.ruedas: int = ruedas
        self.asientos: int = asientos


class Bicicleta(Vehiculo):
    def __init__(self, id_chasis):
        super().__init__("bicicleta", id_chasis, ejes=2, ruedas=2, asientos=1)


bici1 = Bicicleta("A45AGR67")

print(bici1.asientos)
