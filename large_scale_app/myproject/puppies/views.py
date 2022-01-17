
from flask import Blueprint, render_template, redirect, url_for
from myproject import db
from myproject.models import Puppy
from myproject.puppies.forms import AddForm, DelForm

puppies_blueprint = Blueprint('puppies', __name__,
                        template_folder='templates/puppies')

@puppies_blueprint.route('/add', methods=['POST', 'GET'])
def add():
    form = AddForm()

    if form.validate_on_submit():
        name = form.name.data

        # Add new puppy to db
        new_pup = Puppy(name)
        db.session.add(new_pup)
        db.session.commit()

        return redirect(url_for('puppies.list'))
    return render_template('add.html', form=form)

# Delete a puppy entry based on id
def db_del_puppy(id):
    pup = Puppy.query.get(id)
    if pup:
        db.session.delete(pup)
        db.session.commit()
    else:
        print(f"Cannot find a puppy with id={id}")

@puppies_blueprint.route('/list', methods=['GET', 'POST'])
def list():
    puppies = Puppy.query.all()
    delform = DelForm()

    if delform.validate_on_submit():
        id = delform.id.data

        print(f'delete puppy {delform.id.data}')
        db_del_puppy(id)
        return redirect(url_for('puppies.list'))

    return render_template('list.html', puppies=puppies, delform=delform)

@puppies_blueprint.route('/del', methods=['GET', 'POST'])
def delete():
    form = DelForm()

    if form.validate_on_submit():
        id = form.id.data
        db_del_puppy(id)

        return redirect(url_for('puppies.list'))
    return render_template('delete.html', form=form)