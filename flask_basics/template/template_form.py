from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form_home.html')

@app.route('/signup')
def signup():
    return render_template('form_signup.html')

@app.route('/confirm')
def confirm():
    first = request.args.get('first')
    last = request.args.get('last')
    return render_template('form_confirm.html', first=first, last=last)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('form_404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
