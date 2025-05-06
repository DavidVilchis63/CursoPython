#Programacion orientada a objetos

#Clases
class Pajaro:
    
    #Atributos de instancia
    def __init__(self, color, especie):
        self.color = color
        self.especie = especie


#Instancias
miPajaro = Pajaro("verde", "cotorro")
otroPajaro = Pajaro("azul", "guacamaya")


print(miPajaro.color)
print(otroPajaro.color)
print(miPajaro.especie)
print(otroPajaro.especie)
print(type(miPajaro))
