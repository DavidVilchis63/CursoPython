#Manejo de errores


def pedirNumero():

    while True:
        try:
            numero = int(input("Ingresa un numero: "))
        
        except:
            print("Dato incorrecto")
        
        else:
            print(f"Ingresaste un dato correcto {numero}")
            break

    print("Fin programa")


pedirNumero()