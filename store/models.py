from django.db import models

class Product(models.Model):
    Produc_name = models.CharField( max_length=100, unique = True )
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(max_length=500, unique = True)
    price = models.IntegerField()
    image = models.ImageField(upload_to='photos/products')
    stock = models.IntegerField(null = True)
    is_availble = models.BooleanField(default = True)
    
    
    def __str__(self):
        return self.Produc_name 
    
