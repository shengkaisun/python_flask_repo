from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    s = 'Welcome! Go to /puppy_latin/name to see your name in puppy latin!'
    return '<h1> ' + s + '</h1>'

@app.route('/puppy_latin/<name>')
def latin(name):
    if name[-1] == 'y':
        s = name[:-1] + 'iful'
    else:
        s = name + 'y'
    
    r = 'Hi <b>{}</b>! Your puppylatin name is <b>{}</b>'.format(name, s)
    return '<p> ' + r + '</p>'

if __name__ == '__main__':
    app.run(debug=True)