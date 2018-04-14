import pygame
from pygame.locals import *
import sys

pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Pygame Template")

while (1):
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit(0)
