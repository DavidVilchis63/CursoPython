"""
    Modulo pygame
"""

import pygame

pygame.init()

pantalla = pygame.display.set_mode((800,600))

seEjecuta = True

while seEjecuta:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            seEjecuta = False