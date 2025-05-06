#Programacion orientada a objetos

#Clases
class Pajaro:

    #Atributos de clase
    alas = True
    
    #Atributos de instancia
    def __init__(self, color, especie):
        self.color = color
        self.especie = especie


#Instancias
miPajaro = Pajaro("verde", "cotorro")
otroPajaro = Pajaro("azul", "guacamaya")


print(miPajaro.color)
print(miPajaro.especie)
print(otroPajaro.color)
print(otroPajaro.especie)
print(type(miPajaro))
