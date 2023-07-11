import pygame

import sys

import os

from pygame.locals import *


pygame.init()  # initialize pygame

clock = pygame.time.Clock()

screen = pygame.display.set_mode((600, 600))


# Load the background image here. Make sure the file exists!

#bg = pygame.image.load('')

pygame.mouse.set_visible(0)

pygame.display.set_caption('Space Age Game')


# fix indentation

background = (24, 39, 95)

x_earth = 0
y_earth = 0

sun_m = 1.989e30
earth_m = 5.972e24

earth_a = [0, 0]

G = 6.67259e-20

while True:

    clock.tick(60)

    #screen.blit(bg, (0, 0))
    screen.fill(background)

    pygame.draw.circle(screen, (255, 255, 0), (300, 300), 15, 20)



    #x, y = pygame.mouse.get_pos()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


    pygame.display.update()