from planet import planet

class Export:
    def __init__(self):
        self.planets = []

        with open('data_planets.txt', 'r') as f:
            text = f.readlines()
            print(f"text => {text}")
            mas = text.split()

            for i in range(len(mas)):
                if mas[0] == '#':
                    continue
                if len(mas) == 3:
                    name = mas[0]
                    position = float(mas[1])
                    radius = float(mas[2])
                    mass = mas[3]

                    dist_mass = mass.split('E')

                    realMass = dist_mass[0] * (10 ** dist_mass[1])

                    self.planets.append(planet(name, position, radius, realMass))
    
    def GetPlanets(self):
        return self.planets