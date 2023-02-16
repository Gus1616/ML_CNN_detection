from flask import Flask
from flask import request
import tensorflow as tf
from flask_cors import CORS
from flask_restful import Resource, Api, reqparse
import os


app = Flask("DetectionApi")
CORS(app)
api = Api(app)

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

            # Save reference to photo in database or memory
            # ...

            return {'message': 'Photo uploaded successfully'}, 200
        else:
            return {'message': 'No photo was provided'}, 400


api.add_resource(PhotoUpload, '/api/photo/upload')

api.add_resource(Detection, '/api/endpoint')

if __name__ == '__main__':
    app.run()