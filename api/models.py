from django.db import models


# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True,blank=True)
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField(null=True,blank=True)
    seller = models.CharField(max_length=100)
