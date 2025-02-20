#  Argumentos indefinidos

def sumar(*args):
    suma = 0
    for i in args:
        suma += i
    return suma

print(sumar(1,2,3,4,5,6,7,8,9,110))

# Argumentos indefinidos con clave

def sumar(**kwargs):

    total = 0

    for clave, valor in kwargs.items():
        print(f"{clave} = {valor}")
        total += valor

    return total

print(sumar(x=3, y=5, z=2))

