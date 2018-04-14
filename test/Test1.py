import pygame
from pygame.locals import *
import sys
import numpy as np

pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Test")

cells = np.zeros((8, 8))
turn = 1
black = 2
white = 2
font1 = pygame.font.SysFont("microsoftyaheimicrosoftyaheiuibold", 20)
font2 = pygame.font.SysFont("microsoftyaheimicrosoftyaheiuibold", 150)

cells[3, 3] = -1
cells[4, 4] = -1
cells[3, 4] = 1
cells[4, 3] = 1


def put(x, y):
    if cells[x, y] != 0:
        return

    global turn, black, white

    result = False
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i != 0 or j != 0:
                a = 0
                for k in range(1, 8):
                    xxx = x + i * k
                    yyy = y + j * k
                    if (xxx >= 0 and xxx < 8 and yyy >= 0 and yyy < 8):
                        if cells[xxx, yyy] == 0:
                            break
                        elif cells[xxx, yyy] == turn * -1:
                            a = 1
                        else:
                            if a == 1:
                                for l in range(0, k):
                                    cells[x + i * l, y + j * l] = turn
                                result = True
                            break

    if result:
        turn *= -1

    blank = np.sum(cells == 0)
    if blank == 0:
        black = np.sum(cells == 1)
        white = np.sum(cells == -1)
        print("black = %s   white = %s" % (black, white))


while (1):

    screen.fill((0, 100, 0))
    for i in range(0, 8):
        pygame.draw.aaline(screen, (0, 0, 0), (0, 100 * i),
                           (800, 100 * i), False)
        pygame.draw.aaline(screen, (0, 0, 0), (100 * i, 0),
                           (100 * i, 800), False)
    pygame.draw.circle(screen, (0, 0, 0), (201, 201), 5, False)
    pygame.draw.circle(screen, (0, 0, 0), (601, 201), 5, False)
    pygame.draw.circle(screen, (0, 0, 0), (201, 601), 5, False)
    pygame.draw.circle(screen, (0, 0, 0), (601, 601), 5, False)
    for i in range(0, 8):
        for j in range(0, 8):
            if cells[i, j] == 1:
                pygame.draw.circle(screen, (0, 0, 0),
                                   (51 + 100 * i, 51 + 100 * j), 40)
            elif cells[i, j] == -1:
                pygame.draw.circle(screen, (255, 255, 255),
                                   (51 + 100 * i, 51 + 100 * j), 40)
    if pygame.key.get_pressed()[K_TAB]:
        screen.blit(font1.render("black = %s   white = %s" %
                                 (black, white), True, (25, 25, 112)), (3, 0))
    if np.sum(cells == 0) == 0:
        screen.blit(font2.render("Finished!!", True, (255, 0, 0)), (40, 300))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            clickX, clickY = event.pos
            put(clickX // 100, clickY // 100)
        elif event.type == QUIT:
            pygame.quit()
            sys.exit()
