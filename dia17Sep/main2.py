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
Los componentes son suministrados por diversas fábricas.
Una fábrica puede suministrar uno o varios componentes.
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

from importlib.abc import Traversable


class TipoPiezas:
    piezas = ["Motor", "Eje", "Ruedas", "Asientos", "Chasis"]

    def añadir(self, tipoPieza):

        self.piezas.append(tipoPieza)

    def obtener(self, tipoPieza):

        self.piezas.index(tipoPieza)

    def eliminar(self, tipoPieza):

        self.piezas.remove(tipoPieza)

    def modificar(self, tipoPiezaAntigua, tipoPiezaNueva):

        # 1. Buscamos el índice del elemento literal que queremos cambiar
        indice = self.piezas.index(tipoPiezaAntigua)

        # 2. Modificamos ese índice con el nuevo valor
        self.piezas[indice] = tipoPiezaNueva


class Pieza:
    tipo_pieza = []


class Prototipo:
    # atribbutod
    lista_piezas = []


class Camion:
    Tara = 0
    pma = 0


class Autobus:
    num_pasajeros = 0


class Automomvil:
    pass


class Bicicleta:
    pass
