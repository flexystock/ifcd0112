class Fraction:
    def __init__(self, num: int, den: int):
        self.__num = num
        self.__den = den

    def __str__(self) -> str:
        return f"{self.__num} / {self.__den}"

    def gcd(a: int, b: int):
        """AlgoritmodeEuclidesparacalculodelMaximoComunDivisor"""
        while b > 0:
            a, b = b, a % b
            return a
