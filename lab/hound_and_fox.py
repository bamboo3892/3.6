# -*- coding: utf-8 -*-
import numpy as np
import pygame
from pygame.locals import *
from pathlib import Path
import sys


ANGLE_BASE_VECTOR = np.array([0, -1])
WINDOW_SIZE = np.array([1500, 900])
FPS = 100


def calcAngle(vec):
    a0 = np.arccos(np.dot(vec, ANGLE_BASE_VECTOR) / np.linalg.norm(vec))
    return (-1 if np.cross(vec, ANGLE_BASE_VECTOR) > 0 else 1) * a0


def calcVectorFromAngle(angle, length):
    return np.array([np.sin(angle) * length, -np.cos(angle) * length])


def game():
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption("猟犬と狐")
    clock = pygame.time.Clock()

    fontSize = 40
    offset = np.array([fontSize / 2, fontSize / 2])
    sysfont = pygame.font.SysFont(None, fontSize)
    surfaceFox = sysfont.render("F", True, (0, 255, 0))
    surfaceDog = sysfont.render("D", True, (0, 255, 0))

    reset = True
    isPaused = True
    isFinished = False
    # posFox, angleFox, speedFox, isControlledFox
    # posHound, angleHound, speedHound, isControlledHound, n, angleToPastFox

    while(True):
        clock.tick(FPS)

        # reset
        if(reset):
            reset = False
            isPaused = True
            isFinished = False
            posFox = np.array([1000.0, 450.0])
            angleFox = 0.0
            speedFox = 1.0
            isControlledFox = False
            posHound = np.array([500.0, 450.0])
            angleHound = 0.0
            speedHound = 2.0
            isControlledHound = False
            n = 5.0                                         # for Hound B
            angleToPastFox = calcAngle(posFox - posHound)   # for Hound B

        # move
        if(not isPaused and not isFinished):
            # if(not isControlledFox):
            if(not isControlledHound):
                # Hound A
                # angleHound = calcAngle(posFox - posHound)
                # Hound B
                a1 = calcAngle(posFox - posHound)
                angleHound += (a1 - angleToPastFox) * n
                angleToPastFox = a1
            posFox += calcVectorFromAngle(angleFox, speedFox)
            posHound += calcVectorFromAngle(angleHound, speedHound)

        # catch
        if(np.linalg.norm(posHound - posFox) < 20):
            isFinished = True

        # draw
        screen.fill((0, 0, 0,))
        screen.blit(surfaceFox, posFox - offset)
        screen.blit(surfaceDog, posHound - offset)
        pygame.display.update()

        for event in pygame.event.get():
            if (event.type == KEYUP):
                if(event.key == K_SPACE):
                    isPaused = not isPaused
                elif(event.key == K_r):
                    reset = True
            elif(event.type == MOUSEBUTTONDOWN):
                if(event.button == 1):
                    isControlledFox = True
                    angleFox = calcAngle(event.pos - posFox)
                elif(event.button == 3):
                    isControlledHound = True
                    angleHOund = calcAngle(event.pos - posHound)
            elif event.type == QUIT:
                pygame.quit()
                sys.exit(0)
            # elif hound view, fox view?


if __name__ == "__main__":
    game()
    sys.exit(0)
