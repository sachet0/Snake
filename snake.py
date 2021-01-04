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


posX = 240
posY = 240

snakeSurf = pygame.Surface((15, 15))
snakeSurf.fill(white)
snakeRect = snakeSurf.get_rect()
snakeRect.move_ip(posX, posY)
screen.blit(snakeSurf, snakeRect)


def move(keyPress):
    if keyPress == K_UP and snakeRect[1] > 0:
        snakeRect.move_ip(0, -15)
    if keyPress == K_DOWN and snakeRect[1] < 480:
        snakeRect.move_ip(0, 15)
    if keyPress == K_LEFT and snakeRect[0] > 0:
        snakeRect.move_ip(-15, 0)
    if keyPress == K_RIGHT and snakeRect[0] < 480:
        snakeRect.move_ip(15, 0)
    draw()


def draw():
    screen.blit(snakeSurf, snakeRect)
    print("draw called")


keypress = None
oldkey = keypress

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            oldkey = keypress
            if event.key == K_UP and oldkey != K_DOWN:
                keypress = event.key
            if event.key == K_DOWN and oldkey != K_UP:
                keypress = event.key
            if event.key == K_LEFT and oldkey != K_RIGHT:
                keypress = event.key
            if event.key == K_RIGHT and oldkey != K_LEFT:
                keypress = event.key

    screen.fill(black)
    move(keypress)
    pygame.display.update()
    FPS.tick(5)
