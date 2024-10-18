from flask import Flask, render_template, redirect, request
from movies import clearTerminal, get_movies_by_page

app = Flask(__name__)
app.config['ENV'] = "development"
app.config['DEBUG'] = True

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/books')
def books():
    return render_template('books.html')


@app.route('/movies', methods=['POST', 'GET'])
def movies():
    if request.method == 'POST':
        page_number = request.form['movie_page']
        if page_number.isdigit() and int(page_number) > 0 and int(page_number) < 22:
            movies = get_movies_by_page(page_number)['results']
        else:
            movies = get_movies_by_page(1)['results']
    else:
        movies = get_movies_by_page(1)['results']
    return render_template('movies.html', movies = movies)


@app.route('/myportfolio')
def myPortfolio():
    return redirect("https://www.ricardoracines.com")


if __name__ == "__main__":
    app.run()
    