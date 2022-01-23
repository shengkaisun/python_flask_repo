import os 
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
os.environ['OAUTHLIB_RELAX_TOKEN_SCOPE'] = '1'

from flask import Flask, render_template, redirect, url_for
from flask_dance.contrib.google import make_google_blueprint, google

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'

client_id = '948516464908-7c75ai83rd1hjor9c3ejef9udp5js976.apps.googleusercontent.com'
client_secret = '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'
blueprint = make_google_blueprint(client_id=client_id, client_secret=client_secret, 
    offline=True, scope=['profile', 'email'])

app.register_blueprint(blueprint, url_prefix='/login')

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/welcome')
def welcome():
    # Return internal server error if not logged in
    resp = google.get('/oauth2/v2/userinfo')
    assert resp.ok, resp.text
    email = resp.json()['email']
    return render_template('welcome.html', email=email)

@app.route('/login/google')
def login():
    if not google.authorized:
        return render_template(url_for('google.login'))
    resp = google.get('/oauth2/v2/userinfo')
    assert resp.ok, resp.text
    email = resp.json()['email']

    return render_template('welcome.html', email=email)

if __name__ == '__main__':
    app.run(debug=False)