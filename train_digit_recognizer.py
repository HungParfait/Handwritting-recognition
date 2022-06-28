from keras.datasets import mnist
from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Dense, Flatten
# metrics 
from keras.metrics import categorical_crossentropy
# optimization method
from keras.optimizers import SGD
import numpy as np
import matplotlib.pyplot as plt
import random

(X_train, y_train), (X_test, y_test) = mnist.load_data()

def preprocess_data(X_train, y_train, X_test, y_test):
  # reshape images to the required size by Keras
  X_train = X_train.reshape(X_train.shape[0], X_train.shape[1], X_train.shape[2], 1)
  X_test = X_test.reshape(X_test.shape[0], X_test.shape[1], X_test.shape[2], 1)
  # convert from integers to floats
  X_train = X_train.astype('float32')
  X_test = X_test.astype('float32')
  # normalize to range 0-1
  X_train = X_train/255.0
  X_test = X_test/255.0
  # One-hot encoding label 
  y_train = to_categorical(y_train)
  y_test = to_categorical(y_test)
  return X_train, y_train, X_test, y_test 

def LeNet():
  model = Sequential()
  model.add(Conv2D(filters = 6, kernel_size = (5,5), padding = 'same', activation = 'relu', input_shape = (28,28,1)))
  model.add(MaxPooling2D(pool_size = (2,2)))
  model.add(Conv2D(filters = 16, kernel_size = (5,5), activation = 'relu'))
  model.add(MaxPooling2D(pool_size = (2,2)))
  model.add(Flatten())
  model.add(Dense(120, activation = 'relu'))
  model.add(Dense(10, activation = 'softmax'))
  # compile the model with a loss function, a metric and an optimizer function
  opt = SGD(learning_rate = 0.01)
  model.compile(loss = categorical_crossentropy, 
                optimizer = opt, 
                metrics = ['accuracy']) 
  return model

batch_size = 128
epochs = 30

def train_model(model, X_train, y_train, X_test, y_test, epochs = epochs, batch_size = batch_size):
  # Rescaling all training and testing data
  X_train, y_train, X_test, y_test = preprocess_data(X_train, y_train, X_test, y_test)
  # Fitting the model
  history = model.fit(X_train, y_train, epochs = epochs, batch_size = batch_size, steps_per_epoch = X_train.shape[0]//batch_size, validation_data = (X_test, y_test), validation_steps = X_test.shape[0]//batch_size, verbose = 1)
  # evaluate the model
  _, acc = model.evaluate(X_test, y_test, verbose = 1)
  print('Accuracy: %.3f' % (acc * 100.0))
  summary_history(history)

def summary_history(history):
  plt.figure(figsize = (10,6))
  plt.plot(history.history['accuracy'], color = 'blue', label = 'train')
  plt.plot(history.history['val_accuracy'], color = 'red', label = 'val')
  plt.legend()
  plt.title('Accuracy')
  plt.show()

LeNet_model = LeNet()
train_model(LeNet_model, X_train, y_train, X_test, y_test)

LeNet_model.save('handwriting.h5')
print('Successfully. Saving the model as handwriting.h5')

score = LeNet_model.evaluate(X_test, y_test, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])