from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    name = 'Jerry'
    letters = list(name)
    pup_dic = {'pup_name':'Sammy'}
    puppies = ['Ruduf', 'Sam', 'Tutu']
    return render_template('basic.html', name = name, 
        letters = letters, pup_dic = pup_dic, puppies = puppies)

if __name__ == '__main__':
    app.run(debug=True)