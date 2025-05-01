

#Modulos usados
from pathlib import Path
import os

ruta = Path(Path.home(), "Documents", "Python", "Dia 06", "Ejercicio06", "Recetas")

def crearCategoria():
    nuevaCategoria = input("Nombre de la nueva categoria: ")
    (ruta / nuevaCategoria).mkdir()

crearCategoria()