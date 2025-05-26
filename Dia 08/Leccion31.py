"""
    Docoradores
    Un decorador es una función que se utiliza para modificar el comportamiento de otra función.
    Se utiliza el símbolo @ antes de la definición de la función que se quiere decorar.   
"""

def decorarSaludo(funcion):

    def otraFuncion(palabra):
        print("Hola")
        funcion(palabra)
        print("Adios")
    return otraFuncion

#@decorarSaludo
def mayuscula(texto):
    print(texto.upper())

#@decorarSaludo
def minuscula(texto):
    print(texto.lower())

mayusculaDecorada = decorarSaludo(mayuscula)
mayusculaDecorada("Hola Mundo")