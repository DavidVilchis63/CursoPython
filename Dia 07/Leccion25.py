#Polimorfismo


class Vaca:

    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + " Dice muuuu")

class Oveja:

    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + " Dice beeee")

vaca01 = Vaca("Aurora")
oveja01 = Oveja("Nube")

#Ejemplo 1

animales = [vaca01, oveja01]

for animal in animales:
    animal.hablar()

#Ejemplo 2

def animalHabla(animal):
    animal.hablar()

animalHabla(oveja01)