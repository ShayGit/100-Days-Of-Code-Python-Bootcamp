from random import randint

from flask import Flask

app = Flask(__name__)



@app.route('/')
def home():
    return '<h1>Guess a number between 0 and 9</h1>'\
            '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" width=200/>'

@app.route('/<int:number>')
def guess(number):
    if rand_num > number:
        return '<h1>Too Low</h1>' \
               '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" width=200/>'
    elif rand_num < number:
        return '<h1>Too High</h1>' \
               '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" width=200/>'
    else:
        return '<h1>You found me!</h1>'\
                '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" width=200/>'


if __name__ == "__main__":
    rand_num = randint(1, 10)
    app.run(debug=True)
