# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 20:38:20 2019

@author: USER
"""

#  Build a CNN for image classification


import pandas as pd
import numpy as np

from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense


#CNN model

model = Sequential()

model.add(Convolution2D(24, (3,3) , activation = 'relu', input_shape = (64,64,3)))

model.add(MaxPooling2D(pool_size = (2,2)))
model.add(Flatten())

# Add full connection

model.add(Dense(units = 128, activation = 'relu', kernel_initializer = 'uniform'))

model.add(Dense(units = 12, activation = 'softmax'))

model.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])

# fitting the CNN to data
from keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)

test_datagen = ImageDataGenerator(rescale=1./255)

training_set = train_datagen.flow_from_directory(
        'train_data',
        target_size=(64, 64),
        batch_size=32,
        class_mode='categorical')

testing_set = test_datagen.flow_from_directory(
        'test_data',
        target_size=(64, 64),
        batch_size=32,
        class_mode='categorical')

model.fit_generator(
        training_set,
        steps_per_epoch=4714,
        epochs=3,
        validation_data=testing_set,
        validation_steps=825)

model.save('weed_identification_model_softMax')



