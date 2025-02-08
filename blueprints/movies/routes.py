from flask import Blueprint, request, render_template
from blueprints.movies.movies import get_movies_by_page
from models.movies import Movie


movies_bp = Blueprint('movies_bp', __name__, template_folder='../../templates/movies')


@movies_bp.route('/movies', methods=['POST', 'GET'])
def movies():    
    try:
        page_number = request.form['movie_page']
    except:
        page_number = 0
        
    if Movie.is_page_consulted(page_number):
        movies = Movie.get_movies_from_db(page_number)
    else:
        movies = get_movies_by_page(page_number)
        Movie.add_data_to_movies_db(movies, page_number)
    
    return render_template('movies.html', movies = movies)



@movies_bp.route('/movies_db', methods={'POST', 'GET'})
def movies_db():
    movies = Movie.get_all_movies_from_db()
    
    try:
        movies = Movie.get_matching_movies(request.form['query']) 
    except:
        print('No matches found')
    
    return render_template('movies_db.html', movies = movies)