"""
    Archivos zip, comprimir y descomprimir
"""


import zipfile
import shutil

#Generar un archivo comprimido
miZip = zipfile.ZipFile("archivo_comprimido", "w")
miZip.write("mi_texto_A.txt")
miZip.write("mi_texto_B.txt")

miZip.close()

#Abrir un archivo comprimido
zipZbierto = zipfile.ZipFile("archivo_comprimido", "r")
zipZbierto.extractall()

#Comprimir archivos
shutil.make_archive("Nombre del archivo que se genera", "zip" , "ruta")

#Descomprimir
shutil.unpack_archive("Nombre del archivo que se descomprimira", "Nombre de la carpeta que se genera al descomprimir" , "zip")
