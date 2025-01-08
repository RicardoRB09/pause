from flask import Flask, render_template, redirect, request
from movies import get_movies_by_page
from books import scrapBooksByPage
from models import delete_movie_database, init_movies_database, add_data_to_movies_db, is_page_consulted, get_movies_from_db
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
   
    books = scrapBooksByPage(page_number)
    return render_template('books.html', books = books)



@app.route('/movies', methods=['POST', 'GET'])
def movies():    
    try:
        page_number = request.form['movie_page']
    except:
        page_number = 0
        
    if is_page_consulted(page_number):
        movies = get_movies_from_db(page_number)
    else:
        movies = get_movies_by_page(page_number)
        add_data_to_movies_db(movies, page_number)
    
    return render_template('movies.html', movies = movies)



@app.route('/myportfolio')
def myPortfolio():
    return redirect("https://www.ricardoracines.com")



if __name__ == "__main__":
    delete_movie_database()
    init_movies_database()
    app.run()
    