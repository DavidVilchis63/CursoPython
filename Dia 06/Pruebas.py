

#Modulos usados
from pathlib import Path
import os

ruta = Path(Path.home(), "Documents", "Python", "Dia 06", "Ejercicio06", "Recetas")

def mostrasCategorias():
    categorias = []
    for categoria in ruta.iterdir():
        if categoria.is_dir():
            categorias.append(categoria.name)
    print("Categorias:")
    for categoria in categorias:
        print(f"📁 {categoria}")

mostrasCategorias()