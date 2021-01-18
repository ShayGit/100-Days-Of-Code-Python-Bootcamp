from flask import Flask, render_template
import random
from datetime import datetime
import requests

AGIFY_URL = "https://api.agify.io"
GENDERIZE_URL = "https://api.genderize.io"

app = Flask(__name__)


@app.route('/')
def home():
    num = random.randint(1, 10)
    return render_template("index.html", num=num, year=datetime.now().year)


@app.route('/guess/<name>')
def guess(name):
    params = {
        "name": name
    }
    response1 = requests.get(AGIFY_URL, params)
    response2 = requests.get(GENDERIZE_URL, params)

    return render_template("guess.html", name=name, age=response1.json()["age"], gender=response2.json()["gender"])


@app.route('/blog')
def blog():
    blog_url = "https://api.npoint.io/4abe9e61d26745100fed"
    resopnse = requests.get(blog_url)
    posts = resopnse.json()
    print(posts)
    return render_template("blog.html", posts=posts)


if __name__ == "__main__":
    app.run(debug=True)
