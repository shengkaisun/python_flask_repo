
# Set up db inside the __init__.py under myproject folder
from myproject import db

################################
### Models #### 
################################
class Puppy(db.Model):
    __tablename__ = 'puppies'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)

    # Other related tables
    owner = db.relationship('Owner', backref='puppy', uselist=False)
    toys = db.relationship('Toy', backref='puppy', lazy='dynamic')

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        if self.owner:
            return f"Puppy name: {self.name}, owner: {self.owner.name}"
        else:
            return f"Puppy name: {self.name}"

class Owner(db.Model):
    __tablename__ = 'owners'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    puppy_id = db.Column(db.Integer, db.ForeignKey('puppies.id'))

    def __init__(self, name, puppy_id):
        self.name = name
        self.puppy_id = puppy_id
    
    def __repr__(self):
        return f"Owner name: {self.name}"

class Toy(db.Model):
    __tablename__ = 'toys'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    puppy_id = db.Column(db.Integer, db.ForeignKey('puppies.id'))

    def __init__(self, name, puppy_id):
        self.name = name
        self.puppy_id = puppy_id
    
    def __repr__(self):
        return f"Toy name: {self.name}, belongs to puppy id: {self.puppy_id}"
