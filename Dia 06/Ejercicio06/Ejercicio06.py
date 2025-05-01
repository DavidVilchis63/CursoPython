#Creacion de un almacen de recetas

#Modulos usados
from pathlib import Path
import os

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

#Creacion de funciones

#Funcion regresar a menu

def regresarMenu():

    salir = int(input("Presiona 1 para regresar al menu: "))
    if salir == 1:
        limpiarPantalla()
        menu()
    else:
        print("No valido")


#Limpiar pantalla
def limpiarPantalla():
    os.system("cls")

#Mostrar categoria

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

#Mostrar recetas, depende de la seleccion de la categoria

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

#Mostrar contenido de txt

def leerReceta (seleccion, seleccionReceta):
    rutaFinal = Path(ruta, seleccion,seleccionReceta)
    print(rutaFinal.read_text())

#Crear receta

def crearReceta(seleccion):
    nombre = input("Nombre de la receta: ")
    contenido = input("Escriba el contenido de la receta: ")
    rutaNueva = Path(ruta,seleccion)
    nuevaReceta = open(rutaNueva / (nombre+".txt"), "w")
    nuevaReceta.write(contenido)
    nuevaReceta.close()

#Eliminar receta

def eliminarReceta(categoriaElegida, recetaElegida):

    archivoEliminar = Path(ruta, categoriaElegida, recetaElegida)
    archivoEliminar.unlink()
    print(f"Receta {recetaElegida} eliminada")

#Crear categoria

def crearCategoria():
    nuevaCategoria = input("Nombre de la nueva categoria: ")
    (ruta / nuevaCategoria).mkdir()


#Creacion de menu de opciones

def menu():
    print("Elege una de las siguientes opciones: ")
    print("1. Leer receta \n2. Crear receta \n3. Crear categoria \n4. Eliminar receta \n5. Eliminar categoria\n6. Salir")

menu()
opcion = int(input("¿Qué deseas hacer? "))

while opcion != 6:
    if opcion == 1:
        print("Leer receta")    
        categoriaElegida = mostrasCategorias()
        recetaElegida = mostrarRecetas(categoriaElegida)
        leerReceta(categoriaElegida, recetaElegida)
    elif opcion == 2:
        print("Crear receta")
        categoriaElegida = mostrasCategorias()
        crearReceta(categoriaElegida)
    elif opcion == 3:
        print("Crear categoria")
        crearCategoria()
    elif opcion == 4:
        print("Eliminar receta")
        categoriaElegida = mostrasCategorias()
        recetaElegida = mostrarRecetas(categoriaElegida)
        eliminarReceta(categoriaElegida, recetaElegida)
    elif opcion == 5:
        print("Eliminar categoria")
    else:
        print("Opción no válida. Intenta de nuevo.")
        limpiarPantalla()
   
    regresarMenu()
    opcion = int(input("¿Qué deseas hacer? "))

print("Gracias por usar el Admin de Recetas. ¡Hasta luego!")


