#Metodos de clase y estaticos

class Pajaro:

    alas = True
    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    def piar(self):
        print("Pio")

    def volar(self, metros):
        print(f"El pajaro ha volado {metros} metros")
        self.piar()

    def pintar_verde(self):
        self.color = "verde"
        print(f"Ahora el ave es {self.color}")

    #Metodos de clase
    @classmethod
    def ponerHuevos(cls, cantidad):
        print(f"Puso {cantidad} huevos")
        cls.alas = False
        print(Pajaro.alas)

    #Metodos estaticos    
    @staticmethod
    def mirar():
        print("El ave mira")


#Estos metodos  no necesitan una instancia para poder ejecutarse
Pajaro.ponerHuevos(5) 
Pajaro.mirar()
