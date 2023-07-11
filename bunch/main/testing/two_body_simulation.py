import pygame
import sys
import os
from pygame.locals import *

from gravity import gravity
from planet import planet

sun = planet("sun", 0, 1392700, 1.989e30)
earth = planet("earth", 1.496e+11, 6731, 5.972e24)

space = gravity(sun, [earth])

pygame.init()  # initialize pygame

clock = pygame.time.Clock()

screen = pygame.display.set_mode((600, 600))

pygame.mouse.set_visible(0)

pygame.display.set_caption('Space Age Game')

background = (24, 39, 95)

time = 0

while True:
    clock.tick(60)

    screen.fill(background)

    pygame.draw.circle(screen, (255, 255, 0), (300, 300), 15, 20)

    time += 86400 * 365 # this is the number of seconds in 1 day

    #print(f"day number => {time / 86400 / 365}")

    space.get_observation(0, time=86400 * 365 * 500)

    pos = space.getPosition(0)

    print(f"position of earth x => {pos[0]}, earth y => {pos[1]}")
    print(f"screen x position of earth => {300 + pos[0] * 100}, y position of earth => {300 + pos[1] * 100}")

    # for this to be simple let's say that 1 A.U = 100 pixels
    pygame.draw.circle(screen, (55, 243, 174), (300 + pos[0] * 100, 300 + pos[1] * 100), 15, 1)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


    pygame.display.update()