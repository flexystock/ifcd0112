class ListaPersonajes:
    def __init__(self):
        self.__listado_personajes = []

    def add_personaje(self, personaje):
        self.__listado_personajes.append(personaje)
        print("-> Personaje añadido a la lista correctamente.")

    def obtener_todos(self):
        if not self.__listado_personajes:
            print("No hay personajes en la lista.")
        for p in self.__listado_personajes:
            print(p)

    def obtener_tipo_personaje(self, clase_tipo):
        filtrados = [p for p in self.__listado_personajes if isinstance(p, clase_tipo)]
        if not filtrados:
            print("No hay personajes de este tipo.")
        for p in filtrados:
            print(p)

    def obtener_genericos(self):
        # Filtra los que son exactamente de la clase Personaje (excluyendo hijas)
        filtrados = [
            p for p in self.__listado_personajes if type(p).__name__ == "Personaje"
        ]
        if not filtrados:
            print("No hay personajes genéricos.")
        for p in filtrados:
            print(p)
