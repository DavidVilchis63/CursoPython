"""
    Modulo os y shutil
"""

import os
import shutil

print(os.getcwd)    #Ruta de trabajo

ruta = "C:\\Users\\david\\Documents\\Python"

for carpeta, subcarpeta, archivo in os.walk(ruta):

    print(f"En la carpeta: {carpeta}")
    print(f"Las subcarpetas son:")

    for sub in subcarpeta:
        print(f"\t{sub}")

    print("Los archivos son:")
    for arch in archivo:
        print(f"\t{arch}")
    print("\n")