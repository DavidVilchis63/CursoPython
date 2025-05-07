#Herencia multiple

class Padre:

    def hablar(self):
        print("Hola")

class Madre:

    def reir(self):
        print("Risa")

    def hablar(self):
        print("Hola que tal")

class Hijo(Padre, Madre):
    pass

class Nieto(Hijo):
    pass


nieto00 = Nieto()
nieto00.hablar()
nieto00.reir()

#Orden de busqueda de metodos y atributos
print(Nieto.__mro__)