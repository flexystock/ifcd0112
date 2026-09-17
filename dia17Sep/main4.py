"""Define una clase Personaje para representar a los personajes de un juego.
La clase tiene los atributos: nombre del personaje, nivel alcanzado y puntos de vida (llámalos con los nombres de variables que quieras).
Luego, crea las clases hijas: Guerrero y Mago con al menos un parámetro específico para cada una de ellas.

El programa pregunta al usuario si quiere crear un Personaje Guerrero o Mago.
En función de lo que indique el usuario, el programa pide al usuario los datos necesarios para crear el objeto y lo crea.
Finalmente, indica por pantalla que el objeto ha sido creado y pinta los parámetros del objeto."""
# Importamos la clase desde el archivo ListaPersonajes.py

from ListaPersonajes import ListaPersonajes


class Personaje:
    def __init__(
        self, nombre_personaje: str, nivel_alcanzado: int, puntos_de_vida: int
    ):
        self.__nombre_personaje = nombre_personaje
        self.__nivel_alcanzado = nivel_alcanzado
        self.__puntos_de_vida = puntos_de_vida

    def __str__(self):
        return (
            f"Nombre: {self.__nombre_personaje}, "
            f"Nivel: {self.__nivel_alcanzado}, "
            f"Vida: {self.__puntos_de_vida}"
        )


class Guerrero(Personaje):
    def __init__(self, nombre_personaje, nivel_alcanzado, puntos_de_vida, arma):
        super().__init__(nombre_personaje, nivel_alcanzado, puntos_de_vida)
        self.__arma: str = arma

    def __str__(self):
        return super().__str__() + f", Arma: {self.__arma}"


class Mago(Personaje):
    def __init__(self, nombre_personaje, nivel_alcanzado, puntos_de_vida, tipo_poder):
        super().__init__(nombre_personaje, nivel_alcanzado, puntos_de_vida)
        self.__tipo_poder: str = tipo_poder

    def __str__(self):
        return super().__str__() + f", Poder: {self.__tipo_poder}"


if __name__ == "__main__":
    gestor = ListaPersonajes()

    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Crear y añadir Personaje Genérico")
        print("2. Crear y añadir Guerrero")
        print("3. Crear y añadir Mago")
        print("4. Ver todos los personajes")
        print("5. Ver solo Personajes Genéricos")
        print("6. Ver solo Guerreros")
        print("7. Ver solo Magos")
        print("8. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            nombre = input("Nombre del Personaje: ")
            nivel = int(input("Nivel: "))
            vida = int(input("Vida: "))

            personaje = Personaje(nombre, nivel, vida)
            gestor.add_personaje(personaje)
            print("\nObjeto creado:")
            print(personaje)

        elif opcion == "2":
            nombre = input("Nombre del Guerrero: ")
            nivel = int(input("Nivel: "))
            vida = int(input("Vida: "))
            arma = input("Qué arma usa?: ")

            guerrero = Guerrero(nombre, nivel, vida, arma)
            gestor.add_personaje(guerrero)
            print("\nObjeto creado:")
            print(guerrero)

        elif opcion == "3":
            nombre = input("Nombre del Mago: ")
            nivel = int(input("Nivel: "))
            vida = int(input("Vida: "))
            magia = input("Qué tipo de poder usa?: ")

            mago = Mago(nombre, nivel, vida, magia)
            gestor.add_personaje(mago)
            print("\nObjeto creado:")
            print(mago)

        elif opcion == "4":
            print("\n--- Todos los Personajes ---")
            gestor.obtener_todos()

        elif opcion == "5":
            print("\n--- Lista de Personajes Genéricos ---")
            gestor.obtener_genericos()  # ¡Mucho más limpio y sin romper encapsulamiento!

        elif opcion == "6":
            print("\n--- Lista de Guerreros ---")
            gestor.obtener_tipo_personaje(Guerrero)

        elif opcion == "7":
            print("\n--- Lista de Magos ---")
            gestor.obtener_tipo_personaje(Mago)

        elif opcion == "8":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida.")
