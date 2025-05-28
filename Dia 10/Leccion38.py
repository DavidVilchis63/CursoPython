"""
    Modulo pygame
"""

import pygame
import random

#Inicializar pygame
pygame.init()

#Crear pantalla
pantalla = pygame.display.set_mode((800,600))

#Titulo e icono 
pygame.display.set_caption("Invasion Espacial")
icono = pygame.image.load("ovni.png")
pygame.display.set_icon(icono)

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
enemigoY = random.randint(50, 200)
enemigoXCambio = 0

def enemigo(x, y):
    pantalla.blit(imgEnemigo, (x, y))

#Loop del juego
seEjecuta = True

while seEjecuta:

    #Cambiar color de pantalla RGB
    pantalla.fill((205,144,228))

    #Iterar eventos
    for evento in pygame.event.get():

        #Evento para cerrar programa
        if evento.type == pygame.QUIT:
            seEjecuta = False

        #Controlar movimiento de objeto al presionar y soltarflechas
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jugadorXCambio = -0.3
            if evento.key == pygame.K_RIGHT:
                jugadorXCambio = 0.3
        
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugadorXCambio = 0


    #Modifica ubicacion de jugador
    jugadorX += jugadorXCambio

    #Mantener dentro de bordes
    if jugadorX <= 0:
        jugadorX = 0
    elif jugadorX >= 736:
        jugadorX = 736

    #Jugador
    jugador(jugadorX, jugadorY)
    enemigo(enemigoX, enemigoY)

    #Actualiza pantalla
    pygame.display.update()