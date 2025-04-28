#Creacion de un almacen de recetas

#Modulos usados
from pathlib import Path

#Bienvenida al programa

ruta = Path(Path.home(), "Documents", "Python", "Dia 06", "Ejercicio06", "Recetas")
print(ruta)

nombre = input("¿Cuál es tu nombre? ")
print(f"Bienvenido al Admin de Recetas {nombre}")
print("La ruta de la carpeta de recetas es: ", ruta)

conteoRecetas = list(ruta.rglob("*.txt"))    #Contar los archivos .txt en la carpeta para eso sirve glob y rglob para archivos subyacentes
cantidadRecetas = len(conteoRecetas)    #Contar los archivos .txt en la carpeta para eso sirve glob
print("Cantidad de recetas: ", cantidadRecetas)

#for archivo in conteoRecetas:
#    print(archivo)

