import pygame
from pygame.locals import *
import sys
import time
import math
import random
import numpy as np

pygame.init()

# constants
Font = pygame.font.SysFont("microsoftyaheimicrosoftyaheiuibold", 20)
WindowWidth = 800
WindowHeight = 800
PlayerMoveSpeed = 8
PlayerRadius = 20
PlayerBulletSpeed = 40
MonsterMoveSpeed = 4
MonsterRadius = 14
MonsterBulletSpeed = 40
MoveTimeInterval = 1 / 60

pastPastMovedTime = 0
pastMovedTime = time.time()
pastSpawnedTime = pastMovedTime
nextSpawnedSide = 0
ticks = 0
fps = 0
sec = 0

monsterList = []
playerBulletList = []
monsterBulletList = []

playerX = WindowWidth / 2
playerY = WindowHeight / 2
destX = -1
destY = -1

screen = pygame.display.set_mode((WindowWidth, WindowHeight))
pygame.display.set_caption("Game Sample 2D")

while (1):

    # render
    now = time.time()
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (0, 100, 0), (int(playerX), int(playerY)), PlayerRadius, 5)
    for monster in monsterList:
        pygame.draw.circle(screen, (100, 0, 0), (int(monster[0]), int(monster[1])), MonsterRadius, 5)
    screen.blit(Font.render("render fps = %s" % fps, True, (25, 25, 112)), (3, 0))
    screen.blit(Font.render("system fps = %s" % (1 / (pastMovedTime - pastPastMovedTime)), True, (25, 25, 112)),
                (3, 24))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN and event.button == 3:
            destX, destY = event.pos

    # entity move
    if (now > pastMovedTime + MoveTimeInterval):
        if (destX >= 0):
            l = ((destX - playerX) ** 2 + (destY - playerY) ** 2) ** 0.5
            if (l > PlayerMoveSpeed):
                ex = (destX - playerX) / l
                ey = (destY - playerY) / l
                playerX += ex * PlayerMoveSpeed
                playerY += ey * PlayerMoveSpeed
            else:
                playerX = destX
                playerY = destY
                destX = -1
                destY = -1
        mosterlen = len(monsterList)
        for i in range(0, mosterlen):
            monster = monsterList[mosterlen - i - 1]
            monster[0] += MonsterMoveSpeed * math.cos(monster[2])
            monster[1] += MonsterMoveSpeed * math.sin(monster[2])
            if (monster[0] < 0 or monster[0] >= WindowWidth or monster[1] < 0 or monster[1] >= WindowHeight):
                monsterList.pop(mosterlen - i - 1)

        pastPastMovedTime = pastMovedTime
        pastMovedTime = now

    # spawn monster
    monsterSpawnInterval = 1
    if (now > pastSpawnedTime + monsterSpawnInterval):
        l = random.random() * 0.5 + 0.25
        angle = random.random() * math.pi / 2 + math.pi / 4
        if (nextSpawnedSide == 0):
            monsterList.append(np.array([l * WindowWidth, 0, angle]))
            nextSpawnedSide += 1
        elif (nextSpawnedSide == 1):
            monsterList.append(np.array([WindowWidth, l * WindowHeight, angle + math.pi * 0.5]))
            nextSpawnedSide += 1
        elif (nextSpawnedSide == 2):
            monsterList.append(np.array([l * WindowWidth, WindowHeight, angle + math.pi]))
            nextSpawnedSide += 1
        else:
            monsterList.append(np.array([0, l * WindowHeight, angle + math.pi * 1.5]))
            nextSpawnedSide = 0
        pastSpawnedTime = now

    ticks += 1
    if (ticks % 60 == 0):
        fps = 60 / (now - sec)
        sec = now
