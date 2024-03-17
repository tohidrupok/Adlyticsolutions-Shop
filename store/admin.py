from django.contrib import admin
from . models import Product

class ProductAdmin(admin.ModelAdmin): 
     list_display = ['Produc_name', 'price','stock' ,'is_availble']
     
     prepopulated_fields = {'slug' : ('Produc_name',)}
     
admin.site.register(Product, ProductAdmin)