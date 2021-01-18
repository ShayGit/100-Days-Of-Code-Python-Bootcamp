from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    error = None
    if request.method == 'POST':
        name = request.form['username']
        pas = request.form['password']
    else:
        error = 'Invalid username/password'

    return f'<h1> {name}, {pas}</h1>'

if __name__ == "__main__":

    app.run(debug=True)