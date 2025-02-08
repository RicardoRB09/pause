import peewee

db_books = peewee.SqliteDatabase('books.db')

class Book(peewee.Model):
    
    page = peewee.IntegerField()
    title = peewee.TextField()
    price = peewee.TextField()
    description = peewee.TextField()
    image_address = peewee.TextField()
    
    class Meta:
        database = db_books
        
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