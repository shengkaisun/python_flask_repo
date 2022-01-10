# Adoption site
import os
from forms import AddForm, DelForm
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

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Puppy name: {self.name}"

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

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)