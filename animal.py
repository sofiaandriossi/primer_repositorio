class Animal:

    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return f"Animal {self.nombre}"
