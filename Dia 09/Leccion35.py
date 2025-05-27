"""
    Modulos para medir tiempo
"""

import time
import timeit

def pruebaFor(numero):
    lista = []
    for num in range(1, numero + 1):
        lista.append(num)
    return lista

def pruebaWhile(numero):
    lista = []
    contador = 1
    while contador <= numero:
        lista.append(contador)
        contador += 1
    return lista


inicio = time.time()
pruebaFor(100)
final = time.time()
print(final - inicio)

inicio = time.time()
pruebaWhile(100)
final = time.time()
print(final - inicio)