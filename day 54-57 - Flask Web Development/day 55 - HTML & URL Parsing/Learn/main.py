from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"

    return wrapper


def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"

    return wrapper


def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"

    return wrapper

@app.route('/')
@make_bold
@make_emphasis
@make_underlined
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>' \
           '<p> This is a Paragraph</p>' \
           '<img src="https://the-hollywood-gossip-res.cloudinary.com/iu/s--6vtJYYln--/t_full/cs_srgb,f_auto,fl_strip_profile.lossy,q_auto:420/v1383078382/funny-cat-gif.gif" width=200/>'


@app.route('/<name>/<int:number>')
def greet(name, number):
    return f"Hello {name}, {number}"


if __name__ == "__main__":
    app.run(debug=True)
