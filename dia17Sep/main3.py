"""Ejercicio 3: Clase Usuario de Red Social
Crea una clase UsuarioRedSocial para representar a los usuarios de una red social.
La clase tiene los siguientes atributos: el nombre del usuario, una lista de amigos y una lista de publicaciones (llámalos con los nombres de variables que quieras).
La clase debe incluir un método que pinte por pantalla todos los parámetros del objeto UsuarioRedSocial, incluyendo los amigos que tiene y las publicaciones que ha hecho.
El programa pide al usuario que introduzca su nombre, los nombres de 3 amigos y los títulos de 3 publicaciones que haya hecho en la red Social.
A continuación, con los datos introducidos crea un objeto UsuarioRedSocial y pinta por pantalla los parámetros del objeto, empleando el método de la clase UsuarioRedSocial.
"""


class UsuarioRedSocial:
    def __init__(self, nombre_usuario, amigos: list, publicaciones: list):
        self.__nombre_usuario = nombre_usuario
        self.__lista_amigos: list = amigos
        self.__publicaciones = publicaciones

    def __str__(self):
        amigos_str = ", ".join(self.__lista_amigos)
        pubs_str = ", ".join(self.__publicaciones)
        return (
            f"Nombre: {self.__nombre_usuario} \n"
            f"Amigos: [{amigos_str}] \n"
            f"Publicaciones: [{pubs_str}]\n"
        )


nombre_suario = input("Introduzca su nombre:")
# Pedir amigos con un bucle
lista_amigos = []
print("Introduce los nombres de 3 amigos:")
for i in range(3):
    amigo = input(f"Amigo {i + 1}: ")
    lista_amigos.append(amigo)

# Pedir publicaciones de la misma forma
lista_publicaciones = []
print("Introduce los títulos de 3 publicaciones:")
for i in range(3):
    pub = input(f"Publicación {i + 1}: ")
    lista_publicaciones.append(pub)

usuario = UsuarioRedSocial(nombre_suario, lista_amigos, lista_publicaciones)
print("\n--- Datos del Usuario ---")
print(usuario)
