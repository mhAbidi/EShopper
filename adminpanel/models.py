from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100)
    sku = models.CharField( max_length=45)
    short_description = models.CharField( max_length=100)
    long_description = models.CharField(max_length=500)
    price = models.FloatField()
    special_price = models.FloatField()
    quantity = models.IntegerField()
    meta_title = models.CharField(max_length=45)
    meta_description = models.CharField(max_length=400)
    meta_keywords = models.CharField(max_length=400)
