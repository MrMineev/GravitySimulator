import pygame
import copy
import sys
from operations import operations
import math
import numpy
from Body import Body

oper = operations()

# The gravitational constant G
G = 6.67428e-11

AU = (149.6e6 * 1000)     # 149.6 million km, in meters.
#SCALE = 250 / AU

LINE_SCALE = 10

RADIUS_SCALE = 500

class Feature:
    SCALE = 35000 / AU

    MOVEMENT = 10
    ZOOMING = 10000

    FEATURE = 30000

    START = 0

    timestep = 5

    x, y = 0, 0

    angle = 0

    def __init__(self):
        pass

    
    def loop(self, bb, main=None, plot=None, rocket=None):
        bodies = []
        for body in bb:
            b = Body()
            b.px = body.px 
            b.py = body.py 
            b.vx = body.vx 
            b.vy = body.vy 
            b.mass = body.mass
                    
            bodies.append(
                b
            )

        step = 1

        answer = []

        for T in range(self.FEATURE):
            for body in bodies:
                body.prx = body.px
                body.pry = body.py
                body.prvx = body.vx
                body.prvy = body.vy


            step += 1

            force = {}
            for body in bodies:
                # Add up all of the forces exerted on 'body'.
                total_fx = total_fy = 0.0
                for other in bodies:
                    # Don't calculate the body's attraction to itself
                    if body is other:
                        continue
                    fx, fy = body.attraction(other)
                    total_fx += fx
                    total_fy += fy

                # Record the total force exerted.
                force[body] = (total_fx, total_fy)

            # Update velocities based upon on the force.
            for body in bodies:
                fx, fy = force[body]
                body.vx += fx / body.mass * self.timestep
                body.vy += fy / body.mass * self.timestep

                body.px += body.vx * self.timestep
                body.py += body.vy * self.timestep
           
            answer.append(
                (
                    bodies[rocket].px,
                    bodies[rocket].py
                )
            )

        return answer



