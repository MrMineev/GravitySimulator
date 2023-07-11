import tensorflow as tf 
from extract import Extract
import numpy as np

extractor = Extract()

data = extractor.extract()

x_train = data[0]
y_train = data[1]

for i in range(len(y_train)):
    if y_train[i] == 0:
        y_train[i] = 2

index = []
PUMP_DIRECTIONS = 30
for i in range(len(y_train)):
    if y_train[i] == 3 or y_train[i] == 4:
        index.append(i)

for i in range(0, PUMP_DIRECTIONS):
    for j in range(len(index)):
        x_train.append(x_train[index[j]])
        y_train.append(y_train[index[j]])

data = [0, 0, 0, 0, 0]
for i in range(len(y_train)):
    data[y_train[i]] += 1

for i in range(len(data)):
    print(f"{i}: {data[i] / len(y_train) * 100}")

x_train = np.array(x_train)
y_train = np.array(y_train)

print(f"length of input => {len(x_train)}")

x_train = tf.keras.utils.normalize(x_train, axis=1)

model = tf.keras.models.Sequential()

model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dense(2048, activation = tf.nn.relu))
model.add(tf.keras.layers.Dense(516, activation = tf.nn.relu))
model.add(tf.keras.layers.Dense(216, activation = tf.nn.relu))
model.add(tf.keras.layers.Dense(64, activation = tf.nn.relu))
model.add(tf.keras.layers.Dense(5, activation = tf.nn.softmax))

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics='accuracy')

model.fit(x_train, y_train, epochs=30)

model.save('rocket_alpha_1.model')
