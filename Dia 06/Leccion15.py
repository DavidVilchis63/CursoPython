
#Abrir y manipular archivos

miArchivo = open(r"Dia 06\Prueba00.txt")

#print(miArchivo.read())                #Lee todo el archivo y lo imprime

unaLinea = miArchivo.readline()         #Imprime por lineas
print(unaLinea)
unaLinea = miArchivo.readline()         #Imprime la segunda linea porque ya se leyo la primera
print(unaLinea.rstrip())                #Sirve para quitar el salto de linea al final de la cadena
unaLinea = miArchivo.readline()
print(unaLinea)

todasLineas = miArchivo.readlines()     #Lee todas las lineas y las guarda en una lista
print(todasLineas)                      #Imprime la lista completa


miArchivo.close()                       #Cierra el archivo, es importante cerrarlo para liberar recursos del sistema


