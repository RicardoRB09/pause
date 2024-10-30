import requests
from bs4 import BeautifulSoup

books = []

mainUrl = 'https://books.toscrape.com/catalogue/'
baseUrl = 'https://books.toscrape.com/'


class Book:
    def __init__(self, title = '', upc = '', price = '', imageAddress = '', description = ''):
        self.upc = upc
        self.price = price
        self.title = title
        self.imageAddress = imageAddress
        self.description = description  
    
    
def scrapSubPages(subPageIndex):
    newBook = Book()
    response = requests.get(mainUrl+subPageIndex)
    beautifulResponse = BeautifulSoup(response.content, 'html.parser')
    
    newBook.upc = beautifulResponse.find_all("td")[0].text
    newBook.title = beautifulResponse.find('li', class_='active').text
    newBook.price = beautifulResponse.find('p', class_='price_color').text
    newBook.imageAddress = baseUrl + '/'.join(beautifulResponse.find("img").attrs['src'].split('/')[2:])
    newBook.description = beautifulResponse.find('article', class_='product_page').find('p', class_='').text

    books.append(
        {
            'upc' : newBook.upc,
            'title' : newBook.title,
            'price' : newBook.price,
            'imageAddress' : newBook.imageAddress,
            'description' : newBook.description,
        }
    )
    
    

def scrapBooksByPage(page):
    books.clear()
    baseUrl = f'https://books.toscrape.com/catalogue/page-{page}.html'
    print(baseUrl)
    response = requests.get(baseUrl)
    beautifulResponse = BeautifulSoup(response.content, 'html.parser')

    olTagData = beautifulResponse.find('ol', class_='row')
    liFromOlTagData = olTagData.find_all('li')

    for book in liFromOlTagData:
        # print(f'\n\n------------{book}')
        # print(f"\n{book.find('h3').find('a').attrs['href']}")
        scrapSubPages(book.find('h3').find('a').attrs['href'])
    print(books)
    return books
    


