from flask import Flask
from flask_restful import Resource, Api
from security_check import authenticate, identity
from flask_jwt import JWT, jwt_required

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'

api = Api(app)
jwt = JWT(app, authenticate, identity)

puppies = []

class PuppyName(Resource):
    def get(self, name):
        for pup in puppies:
            if pup['name'] == name:
                return pup
        return {'name': None}, 404


    def post(self, name):
        pup = {'name': name}

        puppies.append(pup)
        return pup
    
    def delete(self, name):
        for i, pup in enumerate(puppies):
            if pup['name'] == name:
                puppies.pop(i)
                return {'message': "Delete success"}
        return {'message': "Puppy: " + name + " not found"}, 404

class ListPuppies(Resource):
    @jwt_required()
    def get(self):
        return {'puppies': puppies}

api.add_resource(PuppyName, '/puppy/<string:name>')
api.add_resource(ListPuppies, '/puppies')
        
if __name__ == '__main__':
    app.run(debug=True)