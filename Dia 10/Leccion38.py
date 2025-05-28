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
jugadorXCambio = 0

def jugador(x, y):
    pantalla.blit(imgJugador, (x, y))

#Loop del juego
seEjecuta = True

while seEjecuta:

    #Cambiar color de pantalla RGB
    pantalla.fill((205,144,228))

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            seEjecuta = False

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jugadorXCambio = -0.3
            if evento.key == pygame.K_RIGHT:
                jugadorXCambio = 0.3
        
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugadorXCambio = 0


    #Jugador
    jugadorX += jugadorXCambio
    jugador(jugadorX, JugadorY)

    #Actualiza pantalla
    pygame.display.update()