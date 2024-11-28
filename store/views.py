from django.shortcuts import render, redirect
from products.models import Product

def homepage(request):
    products = Product.objects.all().order_by('-created_at')[:2]
    return render(request, 'index.html', {'products': products})