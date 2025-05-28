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

#Loop del juego
seEjecuta = True

while seEjecuta:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            seEjecuta = False