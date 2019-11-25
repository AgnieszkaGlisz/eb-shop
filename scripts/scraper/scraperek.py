from getHTML import simple_get
from link import url
from book import book
from bs4 import BeautifulSoup
import json
import string


def getBooksLinks(url, link, lastPage):
    for i in range(1, lastPage):
        raw_html = simple_get(url + '?page=' + str(i) + '/')
        html = BeautifulSoup(raw_html, 'lxml')
        divs = html.findAll('div', class_='b-products-list__price-holder')
        #spans = html.findAll('span', class_='b-products-list__sticker-item b-products-list__sticker-item--discount')
        for d in divs:
            link[0].append('https://merlin.pl/' + d.a.get('href'))
        #for s in spans:
            link[1].append(d.span.text)


def getAuthors(html):
    name = ""
    authors = html.findAll('span', class_='product-brand l-product-right-p_bran product-page__product-brand')
    for author in authors:
        tmpname = author.text.replace("\n", "")
        name += tmpname.strip() + ', '
    return name


def getDescription(html):
    description = ""
    descriptions = html.findAll('div', class_='product__main-description')
    for d in descriptions:
        tmpd = d.text.replace("\n", "")
        description += tmpd.strip()
    return description


def bookInfo(html):
    #informations = [] # catalog number, cover, number of pages, ISBN
    #labels = []
    informations = {}
    info = html.html.find('div', id='product-options-list').findAll('div')
    for i in info:
        informations[i.dt.text] = i.dd.text
        #informations.append(i.dd.text)
        #labels.append(i.dd.text)
    return informations


def getBookStatus(html):
    status = ""
    statuses = html.find('div', class_="product-page__badges").findAll('span')
    for s in statuses:
        status += s.text + ' '
    return status


def prices(html, link):
    currentPrice = html.find('span', id="product-price").text.replace("\n", "").replace(" ", "")
    price = html.find('span', id="product-old-price")
    if price != None:
        oldPrice = price.text.replace("\n", "").replace(" ", "")
    else:
        oldPrice = currentPrice
    return currentPrice, oldPrice

def isAvailable(html):
    cartButton = html.find('button', id="add-cart-btn")
    text = cartButton.text
    text = text.strip()
    if text == "do koszyka":
        return True
    else:
        return False

def makebook(title, authors, publisher, category, description, informations, price, currentPrice, discount, status, img):
    book = {}
    book["Title"] = title
    book["Author"] = authors
    book["Publisher"] = publisher
    book["Category"] = category
    book["Description"] = description
    book["Informations"] = informations
    book["Price"] = price
    book["CurrentPrice"] = currentPrice
    book["Discount"] = discount
    book["Status"] = status
    book["Img"] = img
    return book

def getInfoAboutBook(url, discount):
    raw_html = simple_get(url)
    html = BeautifulSoup(raw_html, 'lxml')

    if isAvailable(html) == True:
        title = html.h1.text.replace("\n", "")
        title = title.strip()
        authors = getAuthors(html)
        publisher = html.find('div', class_='product-page__product-categories').p.strong.text
        category = html.find('p', itemprop='category').strong.text.replace("\n", "")
        description = getDescription(html)
        informations = bookInfo(html)  # catalog number, cover, number of pages, ISBN
        currentPrice, oldPrice = prices(html, url)
        status = getBookStatus(html)
        img = html.find('a', class_="is-mobile-hidden").get('href')
        return makebook(title, authors, publisher, category, description, informations, oldPrice, currentPrice, discount, status, img)
    else:
        return None

#info = getInfoAboutBook('https://merlin.pl/frankly-in-love-david-yoon/8263326/')

links = []
linksforreal = []
linkbutpercents = []
links.append(linksforreal)
links.append(linkbutpercents)
for i in range(0, 7):#7
    getBooksLinks(url[i], links, 4)#4
books = []
for i in range(0, len(links[0])):
    info = getInfoAboutBook(links[0][i], links[1][i])
    if info != None:
        books.append(info)
json_data = json.dumps(books, indent=1, sort_keys=False, ensure_ascii=False)
#print(json_data)
with open(r'C:\Users\ooi8\Downloads\hurtownie\biznes\merlin2.json', 'w', encoding="utf16") as outfile:
    json.dump(books, outfile, indent=1, sort_keys=False, ensure_ascii=False)
#print(*links, sep = "\n")
#print(html.prettify())

