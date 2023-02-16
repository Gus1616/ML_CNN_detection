from flask import Flask
from flask import request
import tensorflow as tf
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


filepath = './saved_model'

model = load_model(filepath, compile = True)


class Detection(Resource):

    def get(self):
        return {'message': "Hello From the back end"}



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
            image_files.loc[photo, 'pixels_0':] = image
            image_files = image_files / 255
            test1 = image_files.to_numpy()
            test1 = test1.reshape(-1, 28, 28, 1)
            test1 = np.asarray(test1).astype('float32')
            predictions = model.predict(test1)
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
            



          
            return {'message': label_mapping[classes[0]]}, 200
        else:
            return {'message': 'No photo was provided'}, 400


api.add_resource(PhotoUpload, '/api/photo/upload')

api.add_resource(Detection, '/api/endpoint')

if __name__ == '__main__':
    app.run()