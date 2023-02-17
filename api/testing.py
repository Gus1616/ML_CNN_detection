import tensorflow as tf
tf.config.run_functions_eagerly(True)
import os
import cv2
import pandas as pd

import numpy as np
from keras.models import load_model

image_files = pd.DataFrame(columns=range(784)).add_prefix('pixels_')
r_image = cv2.imread('test_img.jpg')
numpy_image = cv2.cvtColor(r_image, cv2.COLOR_BGR2GRAY)
image = cv2.resize(numpy_image, (28, 28)).astype(np.float32)
image = image.reshape(-1)
image_files.loc[test_img.jpg, 'pixels_0':] = image
image_files = image_files / 255
test1 = image_files.to_numpy()
test1 = test1.reshape(-1, 28, 28, 1)
test1 = np.asarray(test1).astype('float32')
loaded_model = load_model('my_model.h5')
loaded_model.compile(run_eagerly=True)
predictions = loaded_model.predict(test1)
classes = np.argmax(predictions, axis = 1)
label_mapping = {
                    0: 'akiec',
                    1: 'mel',
                    2: 'bkl',
                    3: 'bcc',
                    4: 'nv',
                    5: 'vasc',
                    6: 'df'
                }


