
#Ejercicio 5
#Juego del ahorcado


#Selección de palabra al azar
from random import *

wordList = ["salado", "ejemplo", "programacion", "ahorcado","cinco"]

def elegirPalabra(listaPalabras):
    palabraElegida = choice(listaPalabras)
    letrasUnicas = len(set(palabraElegida))
    return palabraElegida, letrasUnicas

#Inicialización de variables

intentosRestantes = 6
aciertos = 0
letrasCorrectas = []
letrasIncorrectas = []
finJuego = False

#Funciones para el juego

def pedirLetra():
    letraElegida = ""
    esValida = False
    abecedario = "abcdefghijklmnopqrstuvwxyz"

    while not esValida:
        letraElegida = input("Introduce una letra: ").lower()
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
    elif coincidencias == letrasUnicas:
        fin = ganar(palabraOculta)

    return fin, vidas, coincidencias

def perder():
    print("Has perdido")
    print("La palabra era: ", palabra)
    return True

def ganar(palabraDescubierta):
    mostrarTablero(palabraDescubierta)
    print("Has ganado")
    print("La palabra era: ", palabraDescubierta)
    return True

#Inicio del juego
palabra, letrasUnicas = elegirPalabra(wordList)

while not finJuego:
    print("\n" + "*" * 20 + "\n")
    mostrarTablero(palabra)
    print("\n")
    print("Letras incorrectas: ", letrasIncorrectas)
    print(f"Vidas: {intentosRestantes}")
    print("\n" + "*" * 20 + "\n")

    letra = pedirLetra()

    terminado, intentosRestantes, aciertos = chequearLetra(letra, palabra, intentosRestantes, aciertos)

    finJuego = terminado
