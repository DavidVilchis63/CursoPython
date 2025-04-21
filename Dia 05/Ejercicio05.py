
#Ejercicio 5
#Juego del ahorcado


#Selección de palabra al azar
from random import *

wordList = ["python", "ejemplo", "programacion", "ahorcado","cinco"]
randomWord = choice(wordList)

print(randomWord) # borrar al final

#Inicialización de variables

intentosRestantes = 6

palabraOculta = "_" * len(randomWord)
print(palabraOculta) 