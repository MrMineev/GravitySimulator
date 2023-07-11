from operations import operations

operations = operations()

vec = [0, 4]
n = 10

print(operations.multi(n, vec))

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