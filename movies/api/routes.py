from flask import Blueprint, request, jsonify
from movies.helpers import token_required, random_joke_generator
from movies.models import db, Movie, movie_schema, movies_schema


api = Blueprint('api', __name__, url_prefix='/api')


@api.route('/getdata')
def getdata():
    return {'some': 'value'}

#Create movie Endpoint
@api.route('/movies', methods = ['POST'])
@token_required 
def create_movies(our_user):

    name = request.json['name']
    description = request.json['description']
    price = request.json['price']
    release = request.json['release']
    director = request.json['director']
    sequel = request.json['sequel']
    based_on= request.json['based_on']    
    box_office = request.json['box_office']
    series = request.json['series']
    random_joke = random_joke_generator()
    user_token = our_user.token

    print(f"User Token: {our_user.token}")

    movie = Movie(name, description, price, release, director, sequel, based_on, box_office, 
                  series, random_joke, user_token)
    
    db.session.add(movie)
    db.session.commit()

    response = movie_schema.dump(movie)

    return jsonify(response)

#Read 1 Single movie Endpoint
@api.route('/movies/<id>', methods = ['GET'])
@token_required
def get_movie(our_user, id):
    if id:
        movie = Movie.query.get(id)
        response = movie_schema.dump(movie)
        return jsonify(response)
    else:
        return jsonify({'message': 'ID is missing'}), 401
    

#Read all the movies
@api.route('/movies', methods = ['GET'])
@token_required
def get_movies(our_user):
    token = our_user.token
    movies = Movie.query.filter_by(user_token = token).all()
    response = movie_schema.dump(movies)

    return jsonify(response)


#Update 1 Movie by ID
@api.route('/movies/<id>', methods = ['PUT'])
@token_required
def update_movie(our_user,id):
    movie = Movie.query.get(id)

    movie.name = request.json['name']
    movie.demovie.scription = request.json['description']
    movie.price = request.json['price']
    movie.release = request.json['release']
    movie.director = request.json['director']
    movie.sequel = request.json['sequel']
    movie.based_on= request.json['based_on']    
    movie.box_office = request.json['box_office']
    movie.series = request.json['series']
    movie.random_joke = random_joke_generator()
    movie.user_token = our_user.token

   
    db.session.commit()

    response = movie_schema.dump(movie)

    return jsonify(response)


#Delete 1 Movie by ID
@api.route('/movies/<id>', methods = ['DELETE'])
@token_required
def delete_movie(our_user, id):
    movie = Movie.query.get(id)
    db.session.delete(movie)
    db.session.commit()

    response = movies_schema.dump(movie)

    return jsonify(response)


