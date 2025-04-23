#Crear y escribir archivos

archivo = open(r"Dia 06\Prueba00.txt", "w")         #Abre el archivo en modo escritura, si no existe lo crea y si existe lo sobreescribe
archivo.write("Hola Mundo\n")                       #Escribe en el archivo, el \n es para el salto de linea


archivo.writelines(["Hola Mundo", "Hola Mundo2"])   #Escribe varias lineas en el archivo

lista = ["Hola", "Mundo", "Hola", "Mundo2"]       

for p in lista:
    archivo.writelines(p + "\n")                    #Escribe cada elemento de la lista en una nueva linea


archivo.close()             


archivo = open(r"Dia 06\Prueba00.txt", "a")         #Abre el archivo en modo append, si no existe lo crea y si existe lo agrega al final

archivo.write("Bienvenido") 

archivo.close()

