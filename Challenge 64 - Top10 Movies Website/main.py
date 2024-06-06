from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField, IntegerField
from wtforms.validators import DataRequired
import requests
from datetime import datetime

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

class Base(DeclarativeBase):
  pass


class RateMovieForm(FlaskForm):
    rating = FloatField('Your rating out of 10', validators=[DataRequired()])
    review = StringField('Your Review', validators=[DataRequired()])
    submit = SubmitField('Done')

class AddMovieForm(FlaskForm):
    title = StringField('Movie Title', validators=[DataRequired()])
    submit = SubmitField('Add Movie')


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
Bootstrap5(app)

# CREATE DB
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# CREATE TABLE
class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[str] = mapped_column(String(250), nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=True)
    ranking: Mapped[int] = mapped_column(Integer)
    review: Mapped[str] = mapped_column(String(250))
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


with app.app_context():
    db.create_all()

# ADD FIRST ENTRY ON DATABASE
# with app.app_context():
#             new_movie = Movie(
#                         title="Phone Booth",
#                         year=2002,
#                         description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#                         rating=7.3,
#                         ranking=10,
#                         review="My favourite character was the caller.",
#                         img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
# )
#             db.session.add(new_movie)
#             db.session.commit()

# ADD SECOND ENTRY ON DATABASE
# with app.app_context():
#     second_movie = Movie(
#         title="Avatar The Way of Water",
#         year=2022,
#         description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
#         rating=7.3,
#         ranking=9,
#         review="I liked the water.",
#         img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
#     )
#     db.session.add(second_movie)
#     db.session.commit()

@app.route("/")
def home():
    result = db.session.execute(db.select(Movie).order_by(Movie.ranking))
    all_movies = result.scalars().all()
    return render_template('index.html', movies=all_movies)

@app.route('/edit', methods=['GET','POST'])
def edit_rating():
    rate_movie_form = RateMovieForm()  
    movie_id = request.args.get('id')
    movie_selected = db.get_or_404(Movie, movie_id)
    if rate_movie_form.validate_on_submit():  
        movie_selected.rating = request.form.get('rating')
        movie_selected.review = request.form.get('review')
        db.session.commit()  

        return redirect(url_for('home'))  
    
    return render_template("edit.html", form=rate_movie_form, movie=movie_selected, id=movie_id)

@app.route('/delete', methods=['GET','POST'])
def delete():
    movie_id = request.args.get("id")
    movie_to_delete = db.get_or_404(Movie, movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()

    return redirect(url_for('home'))


@app.route('/add', methods=['GET','POST'])
def add_movie():
    add_movie_form = AddMovieForm()
    tmdb_api_key = 'eb5084da6bf7f059e44754b690d36d9c'
    search_movie_endpoint = 'https://api.themoviedb.org/3/search/movie'

    # headers = {
    # "accept": "application/json",
    # "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJlYjUwODRkYTZiZjdmMDU5ZTQ0NzU0YjY5MGQzNmQ5YyIsInN1YiI6IjY2NTJlNWVkMDk0NjJhZWYwMzcxYWFhNSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.KhV-gE62VmNpPmnb6wkksk6mjZbGb7zwiGQ_-Xamiyg"
    # }
    if add_movie_form.validate_on_submit():
        movie_query = add_movie_form.title.data
        params = {
            'query': movie_query,
            'api_key':tmdb_api_key
        }
        response = requests.get(url=search_movie_endpoint, params=params)
        data = response.json()['results']
        return render_template('select.html', options=data)

    return render_template('add.html', form=add_movie_form)

@app.route('/confirm', methods=['GET','POST'])
def confirm_movie():
    movie_id = request.args.get('id')
    if movie_id:
        print(movie_id)
        tmdb_api_key = 'eb5084da6bf7f059e44754b690d36d9c'
        details_endpoint = f'https://api.themoviedb.org/3/movie/{movie_id}'
        response = requests.get(url=details_endpoint, params={'api_key':tmdb_api_key})
        data = response.json()
        print(data)
        selected_movie = Movie(
                    title=data['original_title'],
                    year=int(datetime.strptime(data['release_date'], '%Y-%m-%d').strftime('%Y')),
                    rating=0,
                    ranking=0,
                    review='',
                    description=data['overview'],
                    img_url=f"https://image.tmdb.org/t/p/w500{data['poster_path']}"
        )
        db.session.add(selected_movie)
        db.session.commit()

    return redirect(url_for('edit_rating', id=selected_movie.id))

if __name__ == '__main__':
    app.run(debug=True)
