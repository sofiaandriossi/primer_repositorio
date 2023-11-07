from animales import Animal

class Cetaceo(Animal):

    def __init__(self, oceano, tamanio):
        self.oceano = oceano
        self.tamanio = tamanio

    def __str__(self):
        return f"Cetaceo que vive en el oceano: {self.oceano}"

    def nadar(self):
        return "Nadando..."


class Delfin(Cetaceo):
    pass


class Orca(Cetaceo):
    pass


class BallenaAzul(Cetaceo):
    pass
