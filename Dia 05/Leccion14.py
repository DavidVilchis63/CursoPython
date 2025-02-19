#  Argumentos indefinidos

def sumar(*args):
    suma = 0
    for i in args:
        suma += i
    return suma

print(sumar(1,2,3,4,5,6,7,8,9,110))