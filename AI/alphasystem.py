import math
import random

class AlphaSystem:
    IMPORTANT_CIRCLE = 1.2
    RADIUS = 6731000

    def __init__(self):
        pass

    def important_area(self, x, y):
        if math.sqrt(x ** 2 + y ** 2) < self.RADIUS * self.IMPORTANT_CIRCLE:
            return True 
        return False

    def get_action(self, px, py, vx, vy, angle, engine):
        in_circle = self.important_area(px, py)
        print(f"IN_CIRCLE: {in_circle}")

        if in_circle:
            turn = random.randint(1, 80)
            if turn == 1:
                return 3 
            else:
                return 1
        else:
            return 2

