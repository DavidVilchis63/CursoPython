#Herencia

class Animal:

    def __init__(self, edad, color):
        self.edad = edad
        self.color = color
    def nacer(self):
        print("Este animal ha nacio")

class Pajaro(Animal):
    pass


print(Pajaro.__bases__)
print(Animal.__subclasses__())

#Intancia

ave01 = Pajaro(2,"verde")
ave01.nacer()

print(ave01.color)