from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('exercise_index.html')

def run_check(name):
    results = {"upper":False, "lower":False, "num":False}
    for c in name:
        if c.islower():
            results['lower'] = True
        elif c.isupper():
            results['upper'] = True
        elif c.isdigit():
            results['num'] = True

    return results

@app.route('/username-check')
def check_username():
    username = request.args.get('username')
    results = run_check(username)
    
    return render_template('exercise_check.html', username=username, check=results)

@app.route('/confirm')
def confirm():
    first = request.args.get('first')
    last = request.args.get('last')
    return render_template('form_confirm.html', first=first, last=last)
# Run the web app if directly called
if __name__ == '__main__':
    app.run(debug=True)