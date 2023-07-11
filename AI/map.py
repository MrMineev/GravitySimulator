import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

model = tf.keras.models.load_model('/Users/danila/Documents/space_flight_simulator/rocket_alpha_1.model')

earth = 6731000.00
bottom = [-earth * 2, -earth * 2]
top = [earth * 2, earth * 2]

inc = 10 ** 6 / 2

vx = 0
vy = 0
angle = 90
START = 0

def function(x, y):
    input_layer = [x, y, vx, vy, angle, START]
    qwe = model.predict([input_layer])
    pred = np.argmax(qwe[0])

    return pred

for x in np.arange(bottom[0], top[0], inc):
    for y in np.arange(bottom[1], top[1], inc):
        print(f"X = {x}, Y = {y}")
        response = function(x, y)
        if response == 0:
            plt.plot(x, y, marker='o', color='y')
        elif response == 1:
            plt.plot(x, y, marker='o', color='r')
        elif response == 2:
            plt.plot(x, y, marker='o', color='b')
        else:
            plt.plot(x, y, marker='o', color='g')

plt.show()

