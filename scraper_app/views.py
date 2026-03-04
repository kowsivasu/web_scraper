from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from django.shortcuts import render
from .models import Product, Quote
from urllib.parse import urljoin
from selenium import webdriver
from selenium.webdriver.common.by import By
# Create your views here.


def scrape_books(request):
    url = "https://books.toscrape.com/"
    

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.find_all("article", class_="product_pod")
    
    for book in books:
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text
        stock = book.find("p", class_="instock availability").text
        img_tag = book.find("img")
        img_src = img_tag["src"]

        image_url = urljoin(url,img_src)
        Product.objects.create(title=title, price=price, stock=stock, image=image_url)

    return render(request, "scraper_app/success.html")

def show_books(request):
    books = Product.objects.all()
    return render(request, "scraper_app/show.html", {"books": books})

def show_quotes(request):
    products = Product.objects.all()
    return render(request, "scraper_app/quote.html", {"products": products})


def scrape_quote(request):

    quote_url = "https://quotes.toscrape.com/"
    response = requests.get(quote_url)
    soup = BeautifulSoup(response.text, "html.parser")

    quotes = soup.find_all("div", class_="quote")

    for q in quotes:   # change variable name

        text_tag = q.find("span", class_="text")
        author_tag = q.find("small", class_="author")

        if text_tag and author_tag:
            text = text_tag.get_text(strip=True)
            author = author_tag.get_text(strip=True)

            Quote.objects.create(
                quote=text,
                author=author
            )

    return render(request, "scraper_app/success.html")










# def scrape_flipkart(request):
#     url = "https://www.flipkart.com/search?q=mobile"
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, "html.parser")

#     products = soup.find_all("div", class_="lvJbLV")

#     for product in products:
#         name_tag = product.find("div", class_="RG5Slk")
#         price = product.find("div", class_="hZ3P6w DeU9vF")

#         Product.objects.create(title=name_tag, price=price)
#     return render(request, "scraper_app/success.html")


