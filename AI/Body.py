import math

class Body:
    name = 'Body'
    mass = 0
    vx = vy = 0.0
    px = py = 0.0

    G = 6.67428e-11

    color = (0, 0, 0)

    radius = 0

    thrust = 0

    direction = [0,0]
    angle = 0
    
    def attraction(self, other):
        sx, sy = self.px, self.py
        ox, oy = other.px, other.py
        dx = (ox-sx)
        dy = (oy-sy)
        d = math.sqrt(dx**2 + dy**2)

        if d == 0:
            raise ValueError("Collision between objects %r and %r"
                             % (self.name, other.name))

        f = self.G * self.mass * other.mass / (d**2)

        theta = math.atan2(dy, dx)
        fx = math.cos(theta) * f
        fy = math.sin(theta) * f
        return fx, fy
