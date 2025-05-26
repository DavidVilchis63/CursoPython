#Manejo de errores

def suma():
    n1 = int(input("Numero 1: "))
    n2 = int(input("Numero 2: "))

    print(n1 + n2)


try:
    suma()

except TypeError:
    print("Error, diferentes tipos de datos")

except ValueError:
    print("Error, ingreso un dato que no es un numero")

else:
    print("Programa ejecutado")

finally:
    print("Fin del codigo")