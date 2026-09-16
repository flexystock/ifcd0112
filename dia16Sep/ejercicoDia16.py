"""
Ejercicio 1
Realizar un programa que conste de una clase llamada Estudiante,
que tenga como atributos el nombre y la nota del alumno.
Definir los métodos para inicializar sus atributos,
imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no."""


# definimos la clase
class Estudiante:
    # definimos constructor con parametrosa de entrada
    def __init__(self, *nombre: str, nota: float):
        self.__nombre = nombre
        self.__nota = nota

    # imprimimos atributo, usamos getter
    def get_nombre(self):

        return " ".join(self.__nombre)

    # devolvemos la nota
    def get_nota(self):
        return f"{self.__nota:4.2f}"

    # sete de la nota
    def set_nota(self, nota):
        self.__nota = nota

    # seteo del nombre
    def set_nombre(self, *nombre):
        self.__nombre = nombre

    def __str__(self):
        return f"El estudiante {self.get_nombre()} ha obtenido la nota de: {self.get_nota()}"


if __name__ in ("__main__", "ejercicoDia16"):
    estudiante = Estudiante("Santiago", "Fragio", "Moreno", nota=10.0)
    print(estudiante)
