# Crear funciones

def saludar(nombre):
    print(f"Hola {nombre}, bienvenido a Python")

saludar("David") # De esta forma se llama a la función


def multiplicar(numero1, numero2):
    return numero1 * numero2 # Se utiliza return para devolver un valor

resultado = multiplicar(5, 3)
print(resultado) # De esta forma se imprime el resultado de la función


def check_3_cifras(numero):
    return numero in range(100, 1000)

resultado01 = check_3_cifras(5000);
print(resultado01)

def check_3_cifras_en_lista(lista):

    lista_numeros = [];

    for numero in lista:
        if numero in range(100, 1000):
            lista_numeros.append(numero);
        else:
            pass
    return lista_numeros

resultado02 = check_3_cifras_en_lista([700, 10, 910, 100])
print(resultado02)