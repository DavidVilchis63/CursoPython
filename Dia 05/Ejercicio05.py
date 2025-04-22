
#Ejercicio 5
#Juego del ahorcado


#Selección de palabra al azar
from random import *

wordList = ["python", "ejemplo", "programacion", "ahorcado","cinco"]

def elegirPalabra(listaPalabras):
    palabraElegida = choice(listaPalabras)
    letrasUnicas = len(set(palabraElegida))
    return palabraElegida, letrasUnicas

#Inicialización de variables

intentosRestantes = 6
letrasCorrectas = []
letrasIncorrectas = []
finJuego = False

palabraOculta = "_" * len(randomWord)
print(palabraOculta) 

#Funciones para el juego

def pedirLetra():
    letraElegida = ""
    esValida = False