class File:
    def __init__(self, path: str):
        self.__path = path
        self.__content = []

    def add_content(self, content):
        if isinstance(content, list):
            self.__content.extend(content)
        else:
            self.__content.append(content)

    # Alias por compatibilidad si alguna otra parte usa camelCase
    def addContent(self, content):
        self.add_content(content)

    @property
    def size(self):
        return sum(len(str(elemento)) for elemento in self.__content)

    @property
    def info(self):
        return f"{self.__path} [size={self.size}B]"


class MediaFile(File):
    def __init__(self, path, codec, geoloc, duration):
        super().__init__(path)
        self.codec = codec
        self.geoloc = geoloc
        self.duration = duration

    @property
    def info(self):
        # Hace uso del info de la clase base (File) y añade sus propios campos
        base_info = super().info
        return (
            f"{base_info}\n"
            f"Codec: {self.codec}\n"
            f"Geolocalization: {self.geoloc}\n"
            f"Duration: {self.duration}s"
        )


class VideoFile(MediaFile):
    def __init__(self, path, codec, geoloc, duration, dimensions):
        super().__init__(path, codec, geoloc, duration)
        self.dimensions = dimensions

    @property
    def info(self):
        # Hace uso del info de su clase base (MediaFile) y añade las dimensiones
        base_info = super().info
        return f"{base_info}\nDimensions: {self.dimensions}"
