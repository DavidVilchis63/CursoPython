"""
    Generadores
"""

def miFuncion():
    lista = []
    for x in range(1,5):
        lista.append(x * 10)
    return lista


def miGenerador():
    for x in range(1,5):
        yield x * 10

print(miFuncion())      # Llama a la función y devuelve 4
print(miGenerador())    # Llama al generador y devuelve un objeto generador

variableG = miGenerador()

print(next(variableG))  # Llama al generador y devuelve el primer valor (10)
print(next(variableG))
print(next(variableG))
print(next(variableG))
