from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q
from .models import Product, Basket
from .forms import ProductForm

def product_list(request):
    search_query = request.GET.get('q', '')
    products = Product.objects.all()
    if search_query:
        products = products.filter(
            Q(name__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(category__name__icontains=search_query) |
            Q(color__icontains=search_query)
        )
    paginator = Paginator(products, 10)  

    page_number = request.GET.get('page')  
    page_obj = paginator.get_page(page_number)

    return render(request, 'product_list.html', {'page_obj': page_obj, 'search_query': search_query})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product_detail.html', {'product': product})

def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list') 
    else:
        form = ProductForm()

    return render(request, 'create_product.html', {'form': form})

def basket_view(request):
    if not request.user.is_authenticated:
        return redirect('login')  

    basket_items = Basket.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in basket_items)
    context = {
        'basket_items': basket_items,
        'total_price': total_price,
    }
    return render(request, 'basket.html', context)

def add_to_basket(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, id=product_id)
        Basket.objects.create(user=request.user, product=product, quantity=1)
        return redirect('product_list')
    
def remove_from_basket(request, item_id):
    if request.method == 'POST':
        basket_item = get_object_or_404(Basket, id=item_id, user=request.user)
        basket_item.delete()
    return redirect('basket_view')