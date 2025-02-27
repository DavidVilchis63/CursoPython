# Ejercicio practico 2

# Escribe una función (puedes ponerle cualquier nombre quequieras)
# que reciba cualquier palabra como parámetro, y quedevuelva todas sus letras únicas (sin repetir) 
# pero en ordenalfabético.Por ejemplo si al invocar esta función pasamos la palabra"entretenido",
# debería devolver ['d', 'e', 'i', 'n', 'o', 'r', 't']

def deletreo (palabra):

    listaVacia = []
    for letra in palabra:
        listaVacia.append(letra)

    nueva = sorted(set(listaVacia))

    return nueva

print(deletreo("muorcioaelago"))