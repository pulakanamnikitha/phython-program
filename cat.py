import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 10 # frames per second setting
fpsClock = pygame.time.Clock()

# set up the window
DISPLAYSURF = pygame.display.set_mode((400, 400), 0, 32)
pygame.display.set_caption('cat')

YELLOW = (255, 255,255)
catImg = pygame.image.load('cat.png')
catx = 20
caty = 20
direction = 'down'

while True: # the main game loop
    DISPLAYSURF.fill(YELLOW)

    if direction == 'down':
        catx += 10
        if catx == 280:
            direction = 'right'
    elif direction == 'right':
        caty += 10
        if caty == 230:
            direction = 'up'
    elif direction == 'up':
        catx -= 10
        if catx == 10:
            direction = 'left'
    elif direction == 'left':
        caty -= 10
        if caty == 10:
            direction = 'down'

    DISPLAYSURF.blit(catImg, (catx, catx))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)
