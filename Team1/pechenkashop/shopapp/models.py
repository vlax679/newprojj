from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField(upload_to='media/')
    description = models.CharField(max_length=255)