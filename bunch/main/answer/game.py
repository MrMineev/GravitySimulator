import pygame
import sys
import os
from pygame.locals import *

from gravity import gravity
from planet import planet
from operations import operations

from two_body_problem_orbit import solve

operation = operations()

#sun = planet("sun", 0, 1_392_700_000, 2e30, (255, 255, 0), [0, 0])
#earth = planet("earth", 1.5e+11, 6_731_000, 6e24, (0, 247, 255), [0, 3])

sun = planet("sun", [-100, 0], 1_392_700_000, 200000, (255, 255, 0), [0, 0])
earth = planet("earth", [100, 0], 6_731_000, 1, (0, 247, 255), [-0.00005, 0.000005])
mercury = planet("mercury", [0, 100], 6_731_000, 100, (233, 8, 200), [0.00001, 0.0000005])


# speed of the earth around the sun is 29780 m/s

#space = gravity([sun, earth, mercury])

solve([sun, earth, mercury], 10 ** 5 * 5)


'''
pygame.init()  # initialize pygame

clock = pygame.time.Clock()

screen = pygame.display.set_mode((600, 600))

pygame.mouse.set_visible(0)

pygame.display.set_caption('Space Age Game')

game = True

while game:
    for i in range(len(space.planets)):
        pygame.draw.circle(screen, space.planets[i].color, (300 + space.planets[i].x, 300 + space.planets[i].y), 15, 1)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


    pygame.display.update()
'''