"""
    Proyecto del dia 9
    Descomprimir archivo para ver instrucciones
"""
#import shutil

#shutil.unpack_archive("ProyectoDia9", "EjercicioDia09" , "zip")

# Parte 1 usar os para iterar por todo el directorio

import os
import re
from datetime import datetime
import time
import math


ruta = "C:\\Users\\david\\Documents\\Python\\Dia 09\\Ejercicio09\\Mi_Gran_Directorio"

def buscarArchivos(ruta, patron):
    
    inicio = time.time()
    fechaRevision = datetime.today().strftime("%d/%m/%y")
    resultados = []


    for carpeta, subcarpeta, archivo in os.walk(ruta):
        for arch in archivo:
            ruta_completa = os.path.join(carpeta, arch)

            with open(ruta_completa, "r", encoding="utf-8") as f:
                contenido = f.read()                
                coincidencia = re.findall(patron, contenido)

                if coincidencia:
                    for serie in coincidencia:
                        resultados.append((arch, serie))

    if resultados:
        print("-" * 30)
        print(f"Fecha de hoy: {fechaRevision}\n")
        print(f"Archivo\t\t\tNro. Serie")
        print("-" * 10 + "\t\t"+ "-" * 10)
        for archivo, serie in resultados:
            print(f"{archivo}\t\t {serie}" )

    fin = time.time()
    tiempoTotal = math.ceil(fin - inicio)

    cantidadArchivos = len(resultados)
    print(f"Numeros encontrados: {cantidadArchivos}")
    print(f"Duración de busqueda: {tiempoTotal} segundos")
    print("-" * 30)




patronBusqueda = r"\bN\w{3}-\d{5}\b"

buscarArchivos(ruta,patronBusqueda)