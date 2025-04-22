
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

#Funciones para el juego

def pedirLetra():
    letraElegida = ""
    esValida = False
    abecedario = "abcdefghijklmnopqrstuvwxyz"

    while not esValida:
        letra_elegida = input("Introduce una letra: ").lower()
        if len(letraElegida) == 1 and letraElegida in abecedario:
            esValida = True
        else:
            print("Introduce una letra válida")
    
    return letraElegida

def mostrarTablero(palabraElegida):

    listaOculta = []

    for l in palabraElegida:
        if l in letrasCorrectas:
            listaOculta.append(l)
        else:
            listaOculta.append("_")

    print(" ".join(listaOculta))

def chequearLetra(letraELegida, palabraOculta, vidas, coincidencias):

    fin = False

    if letraELegida in palabraOculta:
        letrasCorrectas.append(letraELegida)
        coincidencias += 1
    else:
        letrasIncorrectas.append(letraELegida)
        vidas -= 1

    if vidas == 0:
        fin = perder()
    elif coincidencias == cantidadLetras:
        fin = ganar(palabraOculta)

    return fin, vidas, coincidencias