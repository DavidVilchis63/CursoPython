#Manejo de errores

def suma():
    n1 = int(input("Numero 1: "))
    n2 = int(input("Numero 2: "))

    print(n1 + n2)


try:
    suma()

except:
    print("Error")

else:
    print("Programa ejecutado")

finally:
    print("Fin del codigo")