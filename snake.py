import sys
import os
import random
import pygame
from pygame.locals import *

pygame.init()
res = (500, 500)
FPS = pygame.time.Clock()

black = (0, 0, 0)
white = (255, 255, 255)

screen = pygame.display.set_mode(res)
# pygame.display.set_caption("Snake")
# pygame.display.set_icon(pygame.image.load("tux.png"))
# fruit = pygame.draw.rect(screen, red, (100,100,15,15), width=0)
# snake = pygame.draw.rect(screen, white, (250,250,20,20), width=0)

# PyInstaller required code block
def resource_path(relative_path):
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

posX = 200
posY = 200

snakeSurf = pygame.Surface((20, 20))
snakeSurf.fill(white)
snakeRect = snakeSurf.get_rect()
# print(snakeSurf.get_rect())
snakeRect.move_ip(posX, posY)
screen.blit(snakeSurf, snakeRect)
# snakeRect = [posX, posY, 20 , 20]

def snake():
    screen.blit(snakeSurf, snakeRect)

def move(direction):
    keyPress = pygame.key.get_pressed()
    if keyPress[K_UP] and snakeRect[1] > 0:
        # snakeRect.move_ip(0, -20)
        snakeRect[1] = snakeRect[1] - 20
        # print("Up")
    if keyPress[K_DOWN] and snakeRect[1] < 480:
        # snakeRect.move_ip(0, 20)
        snakeRect[1] = snakeRect[1] + 20
        # print("Down")
    if keyPress[K_LEFT] and snakeRect[0] > 0:
        # snakeRect.move_ip(-20, 0)
        snakeRect[0] = snakeRect[0] - 20
        # print("Left")
    if keyPress[K_RIGHT] and snakeRect[0] < 480:
        # while snakeRect[0] < 480:
        # snakeRect.move_ip(20, 0)
        snakeRect[0] = snakeRect[0] + 20
        draw()
        print("Right", snakeRect)

# def move(dir):
#     if dir == 

def changeDir():
    # while snakeRect
    pass


def draw():
    screen.blit(snakeSurf, snakeRect)
    print("draw called")

keypress = K_RIGHT

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        # if event.type == KEYDOWN:
        #     if event.key == K_UP and snakeRect[1] > 0:
        #         # print("Up")
        #     if event.key == K_DOWN and snakeRect[1] < 480:
        #         # print("Down")
        #     if event.key == K_LEFT and snakeRect[0] > 0:
        #         # print("Left")
        #     if event.key == K_RIGHT and snakeRect[0] < 480:
        #         snakeRect[0] = snakeRect[0] + 20
        #         draw()
        #         print("Right", snakeRect)

    screen.fill(black)
    move(20)
    draw()
    pygame.display.update()
    FPS.tick(10)
