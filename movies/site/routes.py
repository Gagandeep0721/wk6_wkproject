from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from movies.forms import MovieForm
from movies.models import Movie, db 
from movies.helpers import random_joke_generator


site = Blueprint('site', __name__, template_folder='site_templates')


@site.route('/')
def home():
    print('look at this cool project. Would you just look at it')
    return render_template('index.html')

@site.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    movieform = MovieForm()
   
    try:
        if request.method == 'POST' and movieform.validate_on_submit():
            name = movieform.name.data
            description = movieform.description.data
            price = movieform.price.data
            release = movieform.release.data
            director = movieform.director.data
            sequel = movieform.sequel.data
            based_on = movieform.based_on.data            
            box_office = movieform.box_office.data
            series = movieform.series.data

            if movieform.dad_joke.data:
                random_joke = movieform.dad_joke.data
            else:
                random_joke = random_joke_generator()
            user_token = current_user.token 

            movie = Movie(name, description, price, release, director, sequel, 
                          based_on, box_office, series, random_joke, user_token)
            
            db.session.add(movie)
            db.session.commit()

            return redirect(url_for('site.profile'))
        
    except:
        raise Exception('Movie not created, please check your form and try again.')
    
    user_token = current_user.token 
    movies = Movie.query.filter_by(user_token=user_token)

    return render_template('profile.html', form=movieform, movies = movies )
	