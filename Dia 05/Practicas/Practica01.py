
#Ejercicio practico 1

def devolver_distintos(x,y,z):

    suma = x+y+z
    n_impreso = 0

    mayor = max(x,y,z)
    menor = min(x,y,z)

    if x != mayor and x != menor:
        medio = x
    elif y != mayor and y != menor:
        medio = y
    else:
        medio = z

    if suma > 15:
        n_impreso = mayor
    elif suma < 10:
        n_impreso = menor
    elif suma >= 10 and suma <= 15:
        n_impreso = medio       

    return n_impreso, suma

print(devolver_distintos(55,2,3))



