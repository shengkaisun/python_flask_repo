from flask import Flask, render_template, session, redirect, url_for
from flask import flash
from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, DateTimeField, 
                    RadioField, SelectField, TextAreaField, 
                    SubmitField)

from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'

class InfoForm(FlaskForm):
    # Label, and validator
    breed = StringField("What breed is the puppy?", validators=[DataRequired()])
    neutered = BooleanField("Has the puppy been neutered?")
    mood = RadioField("Please choose your mood:", 
            choices=[('mood_one','Happy'), ('mood_two', 'Excited')])
    food_choice = SelectField(u"Pick your favorite food:", 
                    choices=[('chi', 'Chicken'), ('bf', 'Beef'), ('fish', 'Fish')])
    feedback = TextAreaField()
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def index():
    #breed = False
    form = InfoForm()

    if form.validate_on_submit():
        session['breed'] = form.breed.data
        session['neutered'] = form.neutered.data
        session['mood'] = form.mood.data
        session['food'] = form.food_choice.data
        session['feedback'] = form.feedback.data
        flash('Submission success, breed: {}!'.format(session['breed']))
        # Redirect to another page up on submission
        return redirect(url_for('confirm'))
        #breed = form.breed.data
        #form.breed.data = ''
    return render_template('form_fields_index.html', form=form)

@app.route('/confirm')
def confirm():
    return render_template('confirm.html')


if __name__ == '__main__':
    app.run(debug=True)