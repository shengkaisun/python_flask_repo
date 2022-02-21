import imp
import os
from flask import Flask
from flask_restful import Resource, Api
from security_check import authenticate, identity
from flask_jwt import JWT, jwt_required
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'

#####################
# Set up database
#####################
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Migrate(app, db)


api = Api(app)
jwt = JWT(app, authenticate, identity)

#####################
# DB models
class Puppy(db.Model):
    __tablename__ = "puppies"
    name = db.Column(db.String(80), primary_key=True)
    breed = db.Column(db.String(100))

    def __init__(self, name, breed='unknown'):
        self.name = name
        self.breed = breed
    
    def json(self):
        return {'name':self.name, 'breed':self.breed}

#####################

#puppies = []

class PuppyName(Resource):
    def get(self, name):
        #for pup in puppies:
            #if pup['name'] == name:
                #return pup
        # Using DB
        pup = Puppy.query.filter_by(name=name).first()

        if pup:
            return pup.json()
        
        return {'name': None}, 404


    def post(self, name):
        #pup = {'name': name}
        #puppies.append(pup)
        #return pup
        pup = Puppy(name=name)
        db.session.add(pup)
        db.session.commit()
        return pup.json()
    
    def delete(self, name):
        #for i, pup in enumerate(puppies):
        #    if pup['name'] == name:
        #        puppies.pop(i)
        #        return {'message': "Delete success"}
        pup = Puppy.query.filter_by(name=name).first()
        if pup:
            db.session.delete(pup)
            db.session.commit()
            return {'status':'delete success'}
        
        return {'message': "Puppy: " + name + " not found"}, 404

class ListPuppies(Resource):
    #@jwt_required()
    def get(self):
        puppies = Puppy.query.all()
        return [pup.json() for pup in puppies]
        #return {'puppies': puppies}

api.add_resource(PuppyName, '/puppy/<string:name>')
api.add_resource(ListPuppies, '/puppies')
        
if __name__ == '__main__':
    app.run(debug=True)