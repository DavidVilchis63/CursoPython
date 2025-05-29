"""
    Modulo pygame
"""

import pygame
import random
import math

#Inicializar pygame
pygame.init()

#Crear pantalla
pantalla = pygame.display.set_mode((800,600))

#Titulo e icono 
pygame.display.set_caption("Invasion Espacial")
icono = pygame.image.load("ovni.png")
pygame.display.set_icon(icono)
fondo = pygame.image.load("Fondo.jpg")

#Crear jugador
imgJugador = pygame.image.load("cohete.png")
jugadorX = 368
jugadorY = 536
jugadorXCambio = 0

def jugador(x, y):
    pantalla.blit(imgJugador, (x, y))

#Crear enemigo
imgEnemigo = pygame.image.load("enemigo.png")
enemigoX = random.randint(0, 736)
enemigoY = random.randint(0, 200)
enemigoXCambio = 0.5
enemigoYCambio = 50

def enemigo(x, y):
    pantalla.blit(imgEnemigo, (x, y))

#Crear bala
imgBala = pygame.image.load("bala.png")
balaX = 0
balaY = 536
balaXCambio = 0
balaYCambio = 1
balaVisible = False

def dispararBala(x, y):
    global balaVisible
    balaVisible = True
    pantalla.blit(imgBala, (x + 16, y + 10))

#Funcion para detectar colisiones
def colisionPositiva(x1, y1, x2, y2):
    distancia = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))
    if distancia < 27:
        return True
    else:
        False

#Variable para puntaje
puntaje = 0

#Loop del juego
seEjecuta = True

while seEjecuta:

    #Cambiar color de pantalla RGB
    #pantalla.fill((205,144,228))
    #Cambiar fondo por imagen
    pantalla.blit(fondo, (0,0))

    #Iterar eventos
    for evento in pygame.event.get():

        #Evento para cerrar programa
        if evento.type == pygame.QUIT:
            seEjecuta = False

        #Controlar movimiento de objeto al presionar y soltarflechas
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jugadorXCambio = -1
            if evento.key == pygame.K_RIGHT:
                jugadorXCambio = 1

            #Se agrega codigo para bala
            if evento.key == pygame.K_SPACE:
                if not balaVisible:
                    balaX = jugadorX
                    dispararBala(balaX, balaY)

        
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugadorXCambio = 0


    #Modifica ubicacion de jugador
    jugadorX += jugadorXCambio

    #Mantener dentro de bordes al jugador
    if jugadorX <= 0:
        jugadorX = 0
    elif jugadorX >= 736:
        jugadorX = 736

    #Modifica ubicacion de enemigo
    enemigoX += enemigoXCambio

    #Mantener dentro de bordes al enemigo
    if enemigoX <= 0:
        enemigoXCambio = 0.5
        enemigoY += enemigoYCambio
    elif enemigoX >= 736:
        enemigoXCambio = -0.5
        enemigoY += enemigoYCambio
    
    #Movimiento bala
    if balaY <= -64:
        balaY = 500
        balaVisible = False

    if balaVisible:
        dispararBala(balaX, balaY)
        balaY -= balaYCambio

    #Colision
    colision = colisionPositiva(enemigoX, enemigoY, balaX, balaY)
    if colision:
        balaY = 500
        balaVisible = False
        puntaje += 1
        print(puntaje)
        enemigoX = random.randint(0, 736)
        enemigoY = random.randint(0, 200)

    #Jugador
    jugador(jugadorX, jugadorY)
    enemigo(enemigoX, enemigoY)

    #Actualiza pantalla
    pygame.display.update()