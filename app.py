from flask import Flask, render_template, redirect, request
from movies import get_movies_by_page
from books import scrapBooksByPage
# from models import delete_movie_database, init_movies_database, add_data_to_movies_db, is_page_consulted, get_movies_from_db
from models import Movie, Book
import datetime


app = Flask(__name__)
app.config['ENV'] = "development"
app.config['DEBUG'] = True



@app.route('/')
def home():
    return render_template("index.html")



@app.route('/books', methods={'POST', 'GET'})
def books():
    try:
        page_number = request.form['book_page']
    except:
        page_number = 0
        
        
    if Book.is_page_consulted(page_number):
        books = Book.get_books_from_db(page_number)
    else:
        books = scrapBooksByPage(page_number)
        if books:
            Book.add_data_to_books_db(books, page_number)
    
    return render_template('books.html', books = books)



@app.route('/books_db', methods={'POST', 'GET'})
def books_db():
    books = Book.get_all_books_from_db()
    
    try:
        books = Book.get_matching_books(request.form['query']) 
    except:
        print('No matches found')
        
    return render_template('books_db.html', books = books)



@app.route('/movies', methods=['POST', 'GET'])
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



@app.route('/movies_db', methods={'POST', 'GET'})
def movies_db():
    movies = Movie.get_all_movies_from_db()
    return render_template('movies_db.html', movies = movies)



@app.route('/myportfolio')
def myPortfolio():
    return redirect("https://www.ricardoracines.com")



if __name__ == "__main__":
    Movie.delete_movie_database()
    Movie.init_movies_database()
    Book.delete_book_database()
    Book.init_books_database()
    app.run()
    