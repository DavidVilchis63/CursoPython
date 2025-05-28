"""
    Modulo pygame
"""

import pygame

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
JugadorY = 536

def jugador():
    pantalla.blit(imgJugador, (jugadorX, JugadorY))

#Loop del juego
seEjecuta = True

while seEjecuta:

    #Cambiar color de pantalla RGB
    pantalla.fill((205,144,228))

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            seEjecuta = False

    #Jugador
    jugador()

    #Actualiza pantalla
    pygame.display.update()