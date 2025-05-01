

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
    n = 1
    for categoria in categorias:        
        print(f"📁 {n}.{categoria}")
        n +=1 

    seleccion = int(input("Elige el número de la categoría: "))-1
    return categorias[seleccion] 

def mostrarRecetas(seleccion):
    rutaNueva = Path(ruta, seleccion)
    recetas = []
    for receta in rutaNueva.iterdir():
        if receta.is_file():
            recetas.append(receta.name)
    print(f"Recetas de {seleccion}")
    n = 1
    for receta in recetas:        
        print(f"📁 {n}.{receta}")
        n +=1 
    seleccionReceta = int(input("Elige el número de la receta: "))-1
    return recetas[seleccionReceta]

def leerReceta (seleccion, seleccionReceta):
    rutaFinal = Path(ruta, seleccion,seleccionReceta)
    print(rutaFinal.read_text())

def crearReceta(seleccion):
    nombre = input("Nombre de la receta: ")
    contenido = input("Escriba el contenido de la receta: ")
    rutaNueva = Path(ruta,seleccion)
    nuevaReceta = open(rutaNueva / (nombre+".txt"), "w")
    nuevaReceta.write(contenido)

seleccion = mostrasCategorias()
nuevaReceta = crearReceta(seleccion)






""" conteoRecetas = list(ruta.rglob("*.txt"))    #Contar los archivos .txt en la carpeta para eso sirve glob y rglob para archivos subyacentes
cantidadRecetas = len(conteoRecetas)    #Contar los archivos .txt en la carpeta para eso sirve glob
print("Cantidad de recetas: ", cantidadRecetas) """

#for archivo in conteoRecetas:
#    print(archivo)