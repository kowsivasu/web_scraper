from django.urls import path
from . import views

urlpatterns = [
    path('book_scrape/', views.scrape_books, name='scrape'),
    path('quote_scrape/', views.scrape_quote, name='quote_scrape'),
    path("show/", views.show_books, name="show"),
    path("quote_show/", views.show_quotes, name="quote_show"),

]