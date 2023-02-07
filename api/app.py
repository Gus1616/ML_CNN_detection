from flask import Flask
from flask_cors import CORS
from flask_restful import Resource, Api, reqparse

app = Flask("DetectionApi")
CORS(app)
api = Api(app)

class Detection(Resource):

    def get(self):
        return {'message': "Hello From the back end"}


api.add_resource(Detection, '/api/endpoint')

if __name__ == '__main__':
    app.run()