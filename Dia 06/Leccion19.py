#Modulo pathlib 2

from pathlib import Path

base = Path.home()                                                  #Obtiene la ruta del directorio de inicio del usuario
guia = Path(base, "España", "Barcelona", "Sagrada Familia.txt")     #Crea un objeto de tipo Path con la ruta especificada
print(base)
print(guia) 

guia02 = guia.with_name("Guia02.txt")                               #Cambia el nombre del archivo
print(guia02)

