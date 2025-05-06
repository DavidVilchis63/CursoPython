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
        #Acceder a otros metodos
        self.piar()

    #Acceder y modificar atributos del objeto
    def pintar_verde(self):
        self.color = "verde"
        print(f"Ahora el ave es {self.color}")

ave00 = Pajaro("Negro", "Tucan")
ave00.volar(50)
ave00.pintar_verde()

#Medificar el estado de la clase
ave00.alas = False
print(ave00.alas)