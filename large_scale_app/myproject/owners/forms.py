
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class AddForm(FlaskForm):
    name = StringField('Owner Name: ')
    pup_id = IntegerField('Puppy Id: ')
    submit = SubmitField('Add Owner')

class DelForm(FlaskForm):
    id = IntegerField("Id Number of Owner to Remove:")
    submit = SubmitField('Remove Owner')

class EditForm(FlaskForm):
    id = IntegerField("Id")
    name = StringField("Owner Name")
    submit = SubmitField('Update')
