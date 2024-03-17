from django.shortcuts import render
from .models import Product

# Create your views here.

def store(request):
    products = Product.objects.all() 
    return render(request, 'store/store.html', {'products': products})
     
def product_detail(request, product_slug):
    single_product = Product.objects.get(slug = product_slug) 
       
    return render(request, 'store/product-detail.html', {'product' : single_product}) 