# Python
import seaborn as sns
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegressionCV

from keras.models import Sequential
from keras.layers.core import Dense, Activation
from keras.utils import np_utils

import tensorflow as tf
hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()
print(sess.run(hello))


# https://github.com/fastforwardlabs/keras-hello-world/blob/master/kerashelloworld.ipynb
def one_hot_encode_object_array(arr):
  '''One hot encode a numpy array of objects (e.g. strings)'''
  uniques, ids = np.unique(arr, return_inverse=True)
  return np_utils.to_categorical(ids, len(uniques))

try: 
  # load iris data from seaborne built in data set
  iris = sns.load_dataset("iris")
  iris.head()
  sns.pairplot(iris, hue='species');
  X = iris.values[:, :4]
  y = iris.values[:, 4]
  train_X, test_X, train_y, test_y = train_test_split(X, y, train_size=0.5, test_size=0.5, random_state=0)
  lr = LogisticRegressionCV()
  lr.fit(train_X, train_y)
  print("Accuracy = {:.2f}".format(lr.score(test_X, test_y)))
  train_y_ohe = one_hot_encode_object_array(train_y)
  test_y_ohe = one_hot_encode_object_array(test_y)
  model = Sequential()
  model.add(Dense(16, input_shape=(4,)))
  model.add(Activation('sigmoid'))
  model.add(Dense(3))
  model.add(Activation('softmax'))
  model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=["accuracy"])
  model.fit(train_X, train_y_ohe, epochs=100, batch_size=1, verbose=0);
  loss, accuracy = model.evaluate(test_X, test_y_ohe, verbose=0)
  print("Accuracy = {:.2f}".format(accuracy))
except Exception as e:
  print (str(e))
