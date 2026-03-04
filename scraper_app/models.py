from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=300)
    price = models.CharField(max_length=100)
    stock = models.CharField(max_length=300, blank=True)
    image = models.URLField(blank=True)

    def __str__(self):
        return self.title
    
class Quote(models.Model):
    quote = models.CharField(max_length=300)
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.quote