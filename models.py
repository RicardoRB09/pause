import peewee, datetime

image_base_url = 'https://image.tmdb.org/t/p/w200'

db_movies = peewee.SqliteDatabase('movies.db')

class Movie(peewee.Model):
    
    page = peewee.IntegerField()
    title = peewee.TextField()
    release_date = peewee.DateField(default=datetime.datetime.now)
    overview = peewee.TextField()
    image_url = peewee.TextField()
    
    class Meta:
        database = db_movies
        
        
        
def init_movies_database():
    
    if db_movies.is_closed():
        db_movies.connect()
    else:
        db_movies.close()

    db_movies.create_tables([Movie], safe=True)
    
    
    
def delete_movie_database():
    Movie.drop_table()
    
    
    
def is_page_consulted(page):
    movie = Movie.get_or_none(page = page)
    
    if movie is not None:
        return True
    
    return False
    
    
    
def add_data_to_movies_db(movies, page):
    
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
            
            
            
def get_movies_from_db(page):
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
        
    db_movies.close()
    
    return movies_as_json
        
            