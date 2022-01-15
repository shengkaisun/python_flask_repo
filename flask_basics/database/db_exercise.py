# Adoption site
import os
from forms import AddForm, DelForm, EditForm
from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'

################################
### SQL Database Section ###
################################
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'sqlite:///'+ os.path.join(basedir, 'db_adoption_site.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)

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

################################
### View Function ###
################################
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['GET', 'POST'])
def add_pup():
    form = AddForm()
    if form.validate_on_submit():
        name = form.name.data
        new_pup = Puppy(name)
        db.session.add(new_pup)
        db.session.commit()
        return redirect(url_for('list_pup'))

    return render_template('add.html', form=form)

# Delete a puppy entry based on id
def db_del_puppy(id):
    pup = Puppy.query.get(id)
    if pup:
        db.session.delete(pup)
        db.session.commit()
    else:
        print(f"Cannot find a puppy with id={id}")

@app.route('/list', methods=['GET', 'POST'])
def list_pup():
    puppies = Puppy.query.all()
    delform = DelForm()
    if delform.validate_on_submit():
        id = delform.id.data
        db_del_puppy(id)
        return redirect(url_for('list_pup'))

    return render_template('list.html', puppies=puppies, delform=delform)

@app.route('/delete', methods=['GET', 'POST'])
def del_pup():
    form = DelForm()

    if form.validate_on_submit():
        id = form.id.data
        db_del_puppy(id)
        return redirect(url_for('list_pup'))
    
    return render_template('delete.html', form=form)

@app.route('/edit/<id>', methods=['GET', 'POST'])
def edit_pup(id):
    form = EditForm()
    pup = Puppy.query.get(id)

    if form.validate_on_submit():
        #pup = Puppy.query.get(form.id.data)
        if pup:
            pup.name = form.name.data
            # pup.owner = form.owner
            print('Update name: {}'.format(pup.name))
            if form.owner.data:
                if pup.owner:
                    # Update current owner data
                    pup.owner.name = form.owner.data
                else:
                    # Create a new owner entry
                    owner = Owner(form.owner.data, pup.id)
                    db.session.add(owner)
            if form.toy.data:
                toy = Toy(form.toy.data, pup.id)
                db.session.add(toy)
            db.session.commit()
        return redirect(url_for('list_pup'))
    
    form.id.data = id

    if pup:
        form.name.data = pup.name
        if pup.owner:
            form.owner.data = pup.owner.name
        if pup.toys:
            for toy in pup.toys:
                form.toy.data = toy.name

    return render_template('edit.html', pup=pup, form=form)


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)