import pygame
import sys
import os
from pygame.locals import *

from gravity import gravity
from planet import planet
from operations import operations

operation = operations()

#sun = planet("sun", 0, 1_392_700_000, 2e30, (255, 255, 0), [0, 0])
#earth = planet("earth", 1.5e+11, 6_731_000, 6e24, (0, 247, 255), [0, 3])

sun = planet("sun", [-100, 0], 1_392_700_000, 200000, (255, 255, 0), [0, 0])
earth = planet("earth", [100, 0], 6_731_000, 1, (0, 247, 255), [-0.00005, 0.000005])
mercury = planet("mercury", [0, 100], 6_731_000, 100, (233, 8, 200), [0.00001, 0.0000005])


# speed of the earth around the sun is 29780 m/s

#space = gravity([sun, earth, mercury])

def solve(planets, t):
    space = gravity(planets)

    pygame.init()  # initialize pygame

    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((600, 600))

    pygame.mouse.set_visible(0)

    pygame.display.set_caption('Space Age Game')

    background = (24, 39, 95)

    time = 0
    delta_time = 2000

    while True:
        #rate(500)

        print(f"time => {time}")

        clock.tick(60)

        screen.fill(background)

        space.calculate_new_planet_position(0, 1)
        space.calculate_new_planet_position(1, 2)
        space.calculate_new_planet_position(0, 2)
        
        time = time + delta_time

        # for this to be simple let's say that 1 A.U = 100 pixels
        # A.U = 1.496e+11

        AU = 1.496e+11

        print(f"position of sun => x = {space.planets[0].x}, y = {space.planets[0].y}")
        print(f"position of earth => x = {space.planets[1].x}, y = {space.planets[1].y}")

        print(f"position on screen of sun => x = {300 + space.planets[0].x}, y = {300 + space.planets[0].y}")
        print(f"position on screen of earth => x = {300 + space.planets[1].x}, y = {300 + space.planets[1].y}")

        #pygame.draw.circle(screen, space.planets[0].color, (300 + space.planets[0].x, 300 + space.planets[0].y), 15, 1)

        for i in range(len(space.planets)):
            pygame.draw.circle(screen, space.planets[i].color, (300 + space.planets[i].x, 300 + space.planets[i].y), 15, 1)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


        pygame.display.update()

        if time >= t:
            break

solve([sun, earth, mercury], 10 ** 5 * 6)