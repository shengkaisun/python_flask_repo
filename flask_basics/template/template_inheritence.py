from flask import Flask, render_template

#Jinja template docs:https://jinja.palletsprojects.com/en/3.0.x/templates/

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/puppy/<name>')
def puppy(name):
    return render_template('puppy.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)