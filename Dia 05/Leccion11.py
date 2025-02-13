# Crear funciones

def saludar(nombre):
    print(f"Hola {nombre}, bienvenido a Python")

saludar("David") # De esta forma se llama a la función


def multiplicar(numero1, numero2):
    return numero1 * numero2 # Se utiliza return para devolver un valor

resultado = multiplicar(5, 3)
print(resultado) # De esta forma se imprime el resultado de la función