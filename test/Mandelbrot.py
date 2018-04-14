import pygame
from pygame.locals import *
import sys
import numpy as np
import warnings

warnings.filterwarnings('ignore')

WIDTH = 800
d = 4 / WIDTH
centerX = 0
centerY = 0
z = np.zeros((WIDTH, WIDTH))
c = np.zeros((WIDTH, WIDTH))
mask = np.zeros((WIDTH, WIDTH))
tick = 0
mouseX = 0
mouseY = 0
dragging = False
stop = True
renderZ = np.zeros_like(z)

pygame.init()
screen = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Mandelbrot")


def renew():
    global z, renderZ, c, tick, stop
    z = np.zeros((WIDTH, WIDTH))
    renderZ = np.zeros_like(z)
    c_real, c_imag = np.meshgrid(np.linspace(centerX - WIDTH * d / 2, centerX + WIDTH * d / 2, WIDTH),
                                 np.linspace(centerY - WIDTH * d / 2, centerY + WIDTH * d / 2, WIDTH))
    c = c_real + c_imag * 1j
    tick = 0
    stop = True


renew()

while (1):
    if not stop:
        z = z ** 2 + c
        renderZ[abs(z) > 2] = min(255, tick * 5)
        tick += 1
    pygame.surfarray.blit_array(screen, renderZ.T)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN and event.key == K_SPACE:
            stop = not stop
        elif event.type == MOUSEBUTTONDOWN:
            mouseX, mouseY = event.pos
            dragging = True
        elif event.type == MOUSEBUTTONUP:
            x, y = event.pos
            centerX = (mouseX + x) * d / 2
            centerY = (mouseY + y) * d / 2
            d *= max(abs(mouseX - x), abs(mouseY - y)) / WIDTH
            renew()
            dragging = False
