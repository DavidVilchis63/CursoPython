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

#Creacion de menu de opciones

def menu():
    print("Elege una de las siguientes opciones: ")
    print("1. Leer receta \n2. Crear receta \n3. Crear categoria \n4. Eliminar receta \n5. Eliminar categoria\n6. Salir")

menu()
opcion = int(input("¿Qué deseas hacer? "))

while opcion != 6:
    if opcion == 1:
        print("Leer receta")
    elif opcion == 2:
        print("Crear receta")
    elif opcion == 3:
        print("Crear categoria")
    elif opcion == 4:
        print("Eliminar receta")
    elif opcion == 5:
        print("Eliminar categoria")
    else:
        print("Opción no válida. Intenta de nuevo.")

    opcion = int(input("¿Qué deseas hacer? "))

print("Gracias por usar el Admin de Recetas. ¡Hasta luego!")


