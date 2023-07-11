import math
import numpy

class gravity:
    def __init__(self, planets):
        self.planets = planets
        self.G = 6.67408e-11 # N m^2 kg^-2
    
    def minus(pos1, pos2):
        ans = []
        for i in range(len(pos1)):
            ans.append(pos1[i] - pos2[i])
        return ans # the difference between vectors
    
    def magnitude(self, vector):
        return math.sqrt()
    
    def gforce(self, planet1, planet2):
        # Calculate the gravitational force exerted on planet1 by planet2

        r_vec = self.minus([planet1.x, planet1.y], [planet2.x, planet2.y]) # the distance vector between planet1 and planet2
        r_mag = self.magnitude(r_vec) # finding the magnitude of r_vec

        r_hat = self.divide(r_vec, r_mag) # finding the direction of r_vec on a unit circle

        force_mag = self.G * ((planet1.mass * planet2.mass) / (r_mag ** 2)) # the gravitational force on a unit circle
        force_vec = self.multi(-force_mag, r_hat) # the resulting gravitational force

        return force_vec