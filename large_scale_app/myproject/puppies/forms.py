
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class AddForm(FlaskForm):
    name = StringField('Puppy Name:')
    submit = SubmitField('Add Puppy')

class DelForm(FlaskForm):
    id = IntegerField("Id Number of Puppy to Remove:")
    submit = SubmitField('Remove Puppy')

class EditForm(FlaskForm):
    id = IntegerField("Id")
    name = StringField("Puppy Name")
    owner = StringField("Owner")
    toy = StringField("Toy")
    submit = SubmitField('Update')
