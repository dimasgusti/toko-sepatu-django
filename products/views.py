from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Product

def product_list(request):
    products = Product.objects.all()
    paginator = Paginator(products, 10)  

    page_number = request.GET.get('page')  
    page_obj = paginator.get_page(page_number)

    return render(request, 'product_list.html', {'page_obj': page_obj})