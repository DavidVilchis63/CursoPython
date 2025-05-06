class Pajaro:

    #Atributos de clase
    alas = True
    
    #Atributos de instancia
    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    #Metodos
    def piar(self):
        print("Pio")

    def volar(self, metros):
        print(f"El pajaro ha volado {metros} metros")

ave00 = Pajaro("Negro", "Tucan")
ave00.piar()
ave00.volar(50)