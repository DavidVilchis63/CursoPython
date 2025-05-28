"""
    Modulo pygame
"""

import pygame

#Inicializar pygame
pygame.init()

#Crear pantalla
pantalla = pygame.display.set_mode((800,600))

#


#Loop del juego
seEjecuta = True

while seEjecuta:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            seEjecuta = False