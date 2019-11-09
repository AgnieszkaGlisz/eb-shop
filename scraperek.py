from getHTML import simple_get
from link import url
from book import book
from bs4 import BeautifulSoup

def getBooksLinks(url, link, lastPage):
    for i in range(1,lastPage):
        raw_html = simple_get(url + '?page=' + str(i) + '/')
        html = BeautifulSoup(raw_html, 'lxml')
        divs = html.findAll('div', class_='b-products-list__helper')
        for d in divs:
            link.append('https://merlin.pl/' + d.div.a.get('href'))
  
def getAuthors(html):
    name = ""
    authors = html.findAll('span', class_='product-brand l-product-right-p_bran product-page__product-brand') 
    for author in authors:
        name+= author.text.replace("\n", "").replace(" ", "") + ' '
    return name

def getDescription(html):
    description = ""
    descriptions = html.find('div', class_='product__main-description').findAll('p')
    for d in descriptions:
        description+=d.text
    return description

def bookInfo(html):
    informations = [] #catalog number, cover, number of pages, ISBN
    info = html.html.find('div', id='product-options-list').findAll('div')
    for i in info: 
        informations.append(i.dd.text)
    return informations

def getBookStatus(html):
    status = ""
    statuses = html.find('div', class_="product-page__badges").findAll('span')
    for s in statuses:
        status+= s.text + ' '
    return status

def prices(html):
    currentPrice = html.find('span', id="product-price").text.replace("\n", "").replace(" ", "")
    price = html.find('span', id="product-old-price")
    if price != None:
        oldPrice = price.text.replace("\n", "").replace(" ", "")
    else:
        oldPrice = currentPrice 
    return currentPrice, oldPrice

def getInfoAboutBook(url):
    raw_html = simple_get(url)
    html = BeautifulSoup(raw_html, 'lxml')

    title = html.h1.text.replace("\n", "").replace(" ", "")
    authors = getAuthors(html)
    publisher = html.find('div', class_='product-page__product-categories').p.strong.text
    category = html.find('p', itemprop='category').strong.text.replace("\n", "")
    description = getDescription(html)
    informations = bookInfo(html) #catalog number, cover, number of pages, ISBN
    currentPrice, oldPrice = prices(html)

    status = getBookStatus(html)
    img = html.find('a', class_="is-mobile-hidden").get('href')
    return book(title, authors, publisher, category, description, informations, price, currentPrice, status, img)
    
  
getInfoAboutBook('https://merlin.pl/frankly-in-love-david-yoon/8263326/')

#links = []
#getBooksLinks(url[0], links, 3)
#print(*links, sep = "\n")
#print(html.prettify())




