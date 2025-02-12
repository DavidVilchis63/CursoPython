# Ejercicio del día 4
from random import *

print("Hola, cual es tu nombre?")
nombre = input()

print (f"Hola {nombre}, he pensado un numero del 1 al 100, tienes 8 intentos para adivinar ese numero")

numeroRandom = randint(1,100);
#print(numeroRandom)

intentos = 8

while intentos > 0:
    numeroJugador = int(input("Ingresa tu numero: "))

    if (numeroJugador <= 0) or (numeroJugador > 100):
        print("Numero fuera del limite, intenta de nuevo")
        intentos -= 1
    
    elif (numeroJugador > numeroRandom ):
        print("Tu numero es mayor, intenta de nuevo")
        intentos -= 1

    elif (numeroJugador < numeroRandom):
        print("Tu numero en menor,intenta de nuevo")
        intentos -= 1

    elif (numeroJugador == numeroRandom):
        print("Acertaste el numero")
        break;

if intentos == 0:
    print("Sin intentos, perdiste")