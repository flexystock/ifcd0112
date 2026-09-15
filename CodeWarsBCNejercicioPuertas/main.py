class Door:
    def __init__(self, number: int, frequency: int, activate: bool):
        self.__frequency = frequency
        self.__number = number
        self.__activate = activate

    def get_number(self):
        return self.__number

    def get_frequency(self):
        return self.__frequency

    def get_activate(self):
        return self.__activate

    def activateDoor(self):
        self.__activate = True

    def deactivateDoor(self):
        self.__activate = False

    def set_frequency(self, frequency: int):
        self.__frequency = frequency


class ListDoors:
    def __init__(self, doors: list[Door]):
        self.doors = doors


# le ponemos unos valores iniciales
puertas = ListDoors(
    [
        Door(1, 1, True),
        Door(2, 0, False),
        Door(3, 0, False),
        Door(4, 2, True),
        Door(5, 0, False),
        Door(6, 2, True),
        Door(4, 3, True),
        Door(5, 4, False),
        Door(6, 3, True),
    ]
)

print("INICIO -- Estado de todas las puertas:")
for door in puertas.doors:
    print(
        f"Puerta {door.get_number()} | Frecuencia: {door.get_frequency()} | Activa: {door.get_activate()}"
    )

print("\nPROCESO -- Comprobamos las puertas\n")

# Recorremos las puertas
# nos devuelve la posición y el objeto
for i, door1 in enumerate(puertas.doors):
    freq1 = door1.get_frequency()

    # Si la puerta tiene frecuencia distinta != 0
    if freq1 != 0:
        # Miramoms la frecuencia de las siguientes puertas
        for j in range(i + 1, len(puertas.doors)):
            freq2 = puertas.doors[j].get_frequency()

            # Si encontramos otra puerta con la *misma* frecuencia
            if freq2 == freq1:
                """ Activamos y cambiamos la frecuencia de todas las del medio
                Este tipo de for se usa cuando quieres generar una secuencia de números, por ejemplo, para ir desde una posición hasta otra (i + 1 hasta j).
                range(inicio, fin): Crea una lista invisible de números que empieza en inicio y termina justo antes de llegar a fin.
                Si i es 0 y j es 3, range(1, 3) generará los números 1 y 2. 
                La variable k tomará esos valores en cada vuelta para modificar las puertas que están en medio."""
                for k in range(i + 1, j):
                    puertas.doors[k].set_frequency(freq1)
                    puertas.doors[k].activateDoor()
                break  # Paramos de buscar para este láser porque ya encontró su pareja

            # Si encontramos un número distinto antes de cerrar el circuito, se bloquea
            elif freq2 != 0:
                break

print("ESTADO FINAL -- Configuración de los lásers:")
for door in puertas.doors:
    print(
        f"Puerta {door.get_number()} | Frecuencia: {door.get_frequency()} | Activa: {door.get_activate()}"
    )
