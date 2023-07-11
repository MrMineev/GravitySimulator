from planet import planet
import math
import numpy as np
from operations import operations

operations = operations()

# A.U = 1.496e+11

AU = 1.496e+11

def convertToM(n):
    return n * AU

def calcDist(planet_main, planet_add):
    sum = abs(convertToM(planet_main.x) - convertToM(planet_add.x)) ** 2 + abs(convertToM(planet_main.y) - convertToM(planet_add.y)) ** 2
    return math.sqrt(sum)

class gravity:
    def __init__(self, planets):
        self.planets = planets

        self.time = 0

        self.G = 6.67408e-11 # N m^2 kg^-2

        self.delta_time = 2000
        #self.G = 
    
    def minus(self, pos1, pos2):
        ans = []
        for i in range(len(pos1)):
            ans.append(pos1[i] - pos2[i])
        return ans # this is the difference between two vectors
    
    def magnitude(self, vector):
        return math.sqrt(vector[0] ** 2 + vector[1] ** 2) # this is the magnitude of vector
    
    def divide(self, vector, n):
        ans = []
        for i in range(len(vector)):
            ans.append(vector[i] / n)
        return ans # this is vector / n
    
    def multi(self, n, vector):
        ans = []
        for i in range(len(vector)):
            ans.append(vector[i] * n)
        return ans # this is vector * n

    def gforce(self, planet1, planet2):
        # Calculate the gravitational force exerted on planet1 by planet2

        r_vec = self.minus([planet1.x, planet1.y], [planet2.x, planet2.y]) # the distance vector between planet1 and planet2
        r_mag = self.magnitude(r_vec) # finding the magnitude of r_vec

        r_hat = self.divide(r_vec, r_mag) # finding the direction of r_vec on a unit circle

        force_mag = self.G * ((planet1.mass * planet2.mass) / (r_mag ** 2)) # the gravitational force on a unit circle
        force_vec = self.multi(-force_mag, r_hat) # the resulting gravitational force

        return force_vec
    
    def calculate_new_planet_position(self, index1, index2):
        self.planets[index1].force = self.gforce(self.planets[index1],
                                                 self.planets[index2]) # calculating the force of the sun to the earth
        self.planets[index2].force = self.gforce(self.planets[index2],
                                                 self.planets[index1]) # calculating the force of the earth to the earth

        self.planets[index1].momentum = operations.plus(self.planets[index1].momentum,
                                                        operations.multi(self.delta_time, 
                                                                         self.planets[index1].force))
        self.planets[index2].momentum = operations.plus(self.planets[index2].momentum,
                                                        operations.multi(self.delta_time,
                                                                        self.planets[index2].force))

        #new_sun_position = sun_position + space.planets[0].momentum / space.planets[0].mass * delta_time
        new_sun_position = operations.plus([self.planets[index1].x, self.planets[index1].y],
                                            operations.multi(self.delta_time,
                                                            operations.divide(self.planets[index1].momentum,
                                                                              self.planets[index1].mass))) # calculating new position of the sun
        new_planet_position = operations.plus([self.planets[index2].x, self.planets[index2].y],
                                              operations.multi(self.delta_time,
                                                               operations.divide(self.planets[index2].momentum,
                                                                                 self.planets[index2].mass))) # calculating the new position of the earth

        self.planets[index1].x = new_sun_position[0]
        self.planets[index1].y = new_sun_position[1]

        self.planets[index2].x = new_planet_position[0]
        self.planets[index2].y = new_planet_position[1]
    

'''
space.planets[0].force = space.gforce(space.planets[0],
                                          space.planets[1]) # calculating the force of the sun to the earth
    space.planets[1].force = space.gforce(space.planets[1],
                                          space.planets[0]) # calculating the force of the earth to the earth

    space.planets[0].momentum = operations.plus(space.planets[0].momentum,
                                                operations.multi(delta_time,
                                                                 space.planets[0].force))
    space.planets[1].momentum = operations.plus(space.planets[1].momentum,
                                                operations.multi(delta_time,
                                                                 space.planets[1].force))

    #new_sun_position = sun_position + space.planets[0].momentum / space.planets[0].mass * delta_time
    new_sun_position = operations.plus([space.planets[0].x, space.planets[0].y],
                                        operations.multi(delta_time,
                                                         operations.divide(space.planets[0].momentum,
                                                                           space.planets[0].mass))) # calculating new position of the sun
    new_planet_position = operations.plus([space.planets[1].x, space.planets[1].y],
                                          operations.multi(delta_time,
                                                           operations.divide(space.planets[1].momentum,
                                                                             space.planets[1].mass))) # calculating the new position of the earth

    space.planets[0].x = new_sun_position[0]
    space.planets[0].y = new_sun_position[1]

    space.planets[1].x = new_planet_position[0]
    space.planets[1].y = new_planet_position[1]
'''
    




    

