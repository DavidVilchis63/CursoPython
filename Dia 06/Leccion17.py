#Directorios

import os

ruta = os.getcwd()                                                  #Obtiene el directorio de trabajo actual
print(ruta)

ruta = os.chdir(r"C:\Users\david\Documents\Python")                 #Cambia el directorio de trabajo actual

#ruta = os.makedirs(r"C:\Users\david\Documents\Python\Dia 06")      #Crea una carpeta en la ruta especificada


from pathlib import Path

carpeta = Path(r"C:\Users\david\Documents\Python\Dia 06")           #Crea un objeto de tipo Path con la ruta especificada
archivo = open(carpeta / "Prueba00.txt", "r")                       #Abre el archivo en modo lectura
print(archivo.read())                                               #Lee el archivo y lo imprime

archivo.close()                                                     #Cierra el archivo