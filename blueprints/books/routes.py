
from flask import Blueprint, request, render_template
from blueprints.books.books import scrapBooksByPage
from models.books import Book


books_bp = Blueprint('books_bp', __name__, template_folder='../../templates/books')


@books_bp.route('/books', methods={'POST', 'GET'})
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



@books_bp.route('/books_db', methods={'POST', 'GET'})
def books_db():
    books = Book.get_all_books_from_db()
    
    try:
        books = Book.get_matching_books(request.form['query']) 
    except:
        print('No matches found')
        
    return render_template('books_db.html', books = books)

