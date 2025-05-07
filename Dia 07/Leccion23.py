#Herencia

class Animal:

    def __init__(self, edad, color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print("Este animal ha nacio")

    def hablar(self):
        print("Ruido")


class Pajaro(Animal):

    def __init__(self, edad, color, alturaVuelo):
        super().__init__(edad, color)
        self.altuaVuelo = alturaVuelo

    def hablar(self):
        print("Ruido dos")

    def volar(slef, metros):
        print(f"El ave volo {metros} metros")


print(Pajaro.__bases__)
print(Animal.__subclasses__())

#Intancia

ave01 = Pajaro(2,"verde",30)
ave01.hablar()
ave01.volar(20)

print(ave01.color)