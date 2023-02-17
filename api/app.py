from flask import Flask
from flask import request
import tensorflow as tf
tf.config.run_functions_eagerly(True)

from tensorflow import keras

from flask_cors import CORS
from flask_restful import Resource, Api, reqparse
import os
import cv2
import pandas as pd

import numpy as np
from keras.models import load_model

app = Flask("DetectionApi")
CORS(app)
api = Api(app)


# filepath_model = './saved_model'

# model = load_model(filepath_model, compile = True)
# model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'], run_eagerly=True)


# class Detection(Resource):

#     def get(self):
#         return {'message': "Hello From the back end"}



class PhotoUpload(Resource):
    def post(self):
        photo = request.files.get('photo')

        if photo:
            print("hello")
            filename = photo.filename
            file_path = os.path.join('C:/Users/gusbo/Downloads', filename)
            photo.save(file_path)
            image_files = pd.DataFrame(columns=range(784)).add_prefix('pixels_')
            r_image = cv2.imread(file_path)
            numpy_image = cv2.cvtColor(r_image, cv2.COLOR_BGR2GRAY)
            image = cv2.resize(numpy_image, (28, 28)).astype(np.float32)
            image = image.reshape(-1)
            image_files.loc[file_path, 'pixels_0':] = image
            image_files = image_files / 255
            test1 = image_files.to_numpy()
            test1 = test1.reshape(-1, 28, 28, 1)
            test1 = np.asarray(test1).astype('float32')
            loaded_model = load_model('my_model.h5')
            loaded_model.compile(run_eagerly=True)
            predictions = loaded_model.predict(test1)
            classes = np.argmax(predictions, axis = 1)
            label_mapping = {
                                0: 'Actinic keratoses and intraepithelial carcinoma',
                                1: 'melanoma',
                                2: 'benign keratosis-like lesions',
                                3: 'basal cell carcinoma',
                                4: 'melanocytic nevi',
                                5: 'vascular lesions',
                                6: 'dermatofibroma '
                            }
            



          
            return {'message': label_mapping[classes[0]]}, 200
        else:
            return {'message': 'No photo was provided'}, 400


api.add_resource(PhotoUpload, '/api/photo/upload')

# api.add_resource(Detection, '/api/endpoint')

if __name__ == '__main__':
    app.run()