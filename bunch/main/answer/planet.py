class planet:
    def __init__(self, name, position, radius, mass, color, momentum):
        self.name = name
        self.position = position # m
        self.radius = radius # m
        self.mass = mass # kg

        self.color = color

        self.x = position[0]
        self.y = position[1]

        self.momentum = momentum

        self.force = [0, 0]