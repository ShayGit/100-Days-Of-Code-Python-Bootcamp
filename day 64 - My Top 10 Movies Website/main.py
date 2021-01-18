from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

TMDB_API = "YOUR API KEY FOR https://www.themoviedb.org"
SEARCH_URL = 'https://api.themoviedb.org/3'
MOVIE_DB_IMAGE_URL = "https://image.tmdb.org/t/p/w500"

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Secret-Key'
Bootstrap(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String(250), nullable=False)


db.create_all()

class EditForm(FlaskForm):
    rating = StringField('Your Rating out of 10 e.g. 7.5')
    review = StringField("Your Review")
    submit = SubmitField('Done')

class FindMovieForm(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField("Add Movie")

@app.route("/")
def home():
    movies = Movie.query.order_by(Movie.rating).all()
    for i in range(len(movies)):
        # This line gives each movie a new ranking reversed from their order in all_movies
        movies[i].ranking = len(movies) - i
    db.session.commit()
    return render_template("index.html", movies = movies)

@app.route("/edit", methods=['GET','POST'])
def edit():
    edit_form = EditForm()
    movie_id = request.args.get("id")
    movie_selected = Movie.query.get(movie_id)
    if edit_form.validate_on_submit():
        new_rating = edit_form.rating.data
        new_review = edit_form.review.data
        if new_rating:
            movie_selected.rating = float(new_rating)
        if new_review:
            movie_selected.review = new_review
        db.session.commit()
        return redirect(url_for('home'))

    return render_template("edit.html", movie = movie_selected, form =edit_form )

@app.route('/delete')
def delete():
    movie_id = request.args.get("id")
    movie_selected = Movie.query.get(movie_id)
    db.session.delete(movie_selected)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/add', methods=['GET','POST'])
def add():
    add_form = FindMovieForm()
    if add_form.validate_on_submit():
        title = add_form.title.data
        params={
          "api_key": TMDB_API,
            "query": title
        }
        response = requests.get(f"{SEARCH_URL}/search/movie", params)
        data = response.json()["results"]
        return render_template("select.html", options=data)
    return render_template("add.html", form = add_form )

@app.route('/select', methods=['GET','POST'])
def select():
    movie_api_id = request.args.get("id")
    if movie_api_id:
        movie_api_url = f"{SEARCH_URL}/movie/{movie_api_id}"
        response = requests.get(movie_api_url, params={"api_key": TMDB_API, "language": "en-US"})
        data = response.json()
        new_movie = Movie(
            title=data["title"],
            # The data in release_date includes month and day, we will want to get rid of.
            year=data["release_date"].split("-")[0],
            img_url=f"{MOVIE_DB_IMAGE_URL}{data['poster_path']}",
            description=data["overview"]
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for("edit", id=new_movie.id))

if __name__ == '__main__':
    # new_movie = Movie(
    #     title="Phone Booth",
    #     year=2002,
    #     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
    #     rating=7.3,
    #     ranking=10,
    #     review="My favourite character was the caller.",
    #     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
    # )
    # db.session.add(new_movie)
    # db.session.commit()
    app.run(debug=True)
