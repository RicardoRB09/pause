import peewee, datetime

image_base_url = 'https://image.tmdb.org/t/p/w200'

db_movies = peewee.SqliteDatabase('movies.db')
db_books = peewee.SqliteDatabase('books.db')

class Movie(peewee.Model):
    
    page = peewee.IntegerField()
    title = peewee.TextField()
    release_date = peewee.DateField(default=datetime.datetime.now)
    overview = peewee.TextField()
    image_url = peewee.TextField()
    
    class Meta:
        database = db_movies
        
    @classmethod    
    def init_movies_database(cls):
        
        if db_movies.is_closed():
            db_movies.connect()
        else:
            db_movies.close()

        db_movies.create_tables([Movie], safe=True)
        
        
    @classmethod
    def delete_movie_database(cls):
        Movie.drop_table()
        
        
    @classmethod    
    def is_page_consulted(cls, page):
        movie = Movie.get_or_none(page = page)
        
        if movie is not None:
            return True
        
        return False
        
        
    @classmethod    
    def add_data_to_movies_db(cls, movies, page):
        
        for movie in movies:
            try:
                Movie.create(
                    page = page,
                    title = movie['title'],
                    release_date = movie['release_date'],
                    overview = movie['overview'],
                    image_url = image_base_url + movie['poster_path']
                )
            except:
                print(f'Data duplicated')
                continue
                
                
    @classmethod       
    def get_movies_from_db(cls, page):
        movies_as_json = []
        movies = Movie.select().where(Movie.page == page)
        
        for movie in movies:
            print(movie.title)
            movies_as_json.append(
                {
                    'title' : movie.title,
                    'release_date' : movie.release_date,
                    'overview' : movie.overview,
                    'poster_path' : image_base_url + movie.image_url,
                }
            )
        
        return movies_as_json
    
    
    @classmethod       
    def get_all_movies_from_db(cls):
        movies_as_json = []
        movies = Movie.select()
        
        for movie in movies:
            print(movie.title)
            movies_as_json.append(
                {
                    'title' : movie.title,
                    'release_date' : movie.release_date,
                    'overview' : movie.overview,
                    'poster_path' : image_base_url + movie.image_url,
                }
            )
        
        return movies_as_json
    
    
    @classmethod       
    def get_matching_movies(cls, query):
        movies_as_json = []
        movies = Movie.select().where(Movie.title.contains(query))
        
        for movie in movies:
            movies_as_json.append(
                {
                    'title' : movie.title,
                    'release_date' : movie.release_date,
                    'overview' : movie.overview,
                    'poster_path' : image_base_url + movie.image_url,
                }
            )
        
        return movies_as_json
        
        
class Book(peewee.Model):
    
    page = peewee.IntegerField()
    title = peewee.TextField()
    price = peewee.TextField()
    description = peewee.TextField()
    image_address = peewee.TextField()
    
    class Meta:
        database = db_movies
        
    @classmethod    
    def init_books_database(cls):
        
        if db_books.is_closed():
            db_books.connect()
        else:
            db_books.close()

        db_books.create_tables([Book], safe=True)
        
        
    @classmethod
    def delete_book_database(cls):
        Book.drop_table()
        
        
    @classmethod    
    def is_page_consulted(cls, page):
        book = Book.get_or_none(page = page)
        
        if book is not None:
            return True
        
        return False
        
        
    @classmethod    
    def add_data_to_books_db(cls, books, page):
        
        for book in books:
            try:
                Book.create(
                    page = page,
                    title = book['title'],
                    price = book['price'],
                    description = book['description'],
                    image_address = book['imageAddress']
                )
            except:
                print(f'Data duplicated')
                continue
                
                
    @classmethod       
    def get_books_from_db(cls, page):
        books_as_json = []
        books = Book.select().where(Book.page == page)
        
        for book in books:
            print(book.title)
            books_as_json.append(
                {
                    'title' : book.title,
                    'price' : book.price,
                    'description' : book.description,
                    'imageAddress' : book.image_address,
                }
            )
        
        return books_as_json
    
    @classmethod       
    def get_all_books_from_db(cls):
        books_as_json = []
        books = Book.select()
        
        for book in books:
            books_as_json.append(
                {
                    'title' : book.title,
                    'price' : book.price,
                    'description' : book.description,
                    'imageAddress' : book.image_address,
                }
            )
        
        return books_as_json
        
        
    @classmethod       
    def get_matching_books(cls, query):
        books_as_json = []
        books = Book.select().where(Book.title.contains(query))
        
        for book in books:
            books_as_json.append(
                {
                    'title' : book.title,
                    'price' : book.price,
                    'description' : book.description,
                    'imageAddress' : book.image_address,
                }
            )
        
        return books_as_json
        
        
        

        
            