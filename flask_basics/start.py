from flask import Flask

app = Flask(__name__)

@app.route('/') #127.0.0.1:5000
def index():
    return "<h1>Hello Flask!</h1>"

@app.route('/info')
def info():
    return "<h1>Puppies info!</h1>"

# Dynamic route
@app.route('/puppy/<name>')
def puppy(name):
    return "<h1>100th letter: {}</h1>".format(name[100])

if __name__ == '__main__':
    app.run(debug = True)