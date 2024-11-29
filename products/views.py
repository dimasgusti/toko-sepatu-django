from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Product, Basket
from .forms import ProductForm
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

def product_list(request):
    if not request.user.groups.filter(name='user').exists():
        return redirect('account')
    
    search_query = request.GET.get('q', '')
    products = Product.objects.all()

    products = products.filter(stock__gt=0)

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

@login_required
def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('dashboard_admin')
    else:
        form = ProductForm(instance=product)
    return render(request, 'edit_product.html', {'form': form, 'product': product})

@login_required
def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('dashboard_admin')  
    return render(request, 'delete_product.html', {'product': product})

def add_to_basket(request, product_id):
    if not request.user.is_authenticated:
        return redirect('login')

    product = get_object_or_404(Product, id=product_id)
    basket_item, created = Basket.objects.get_or_create(user=request.user, product=product)

    if not created:
        basket_item.quantity += 1
        basket_item.save()

    return redirect('basket_view') 

def update_basket_item(request, item_id):
    if not request.user.is_authenticated:
        return redirect('login')

    basket_item = get_object_or_404(Basket, id=item_id, user=request.user)
    
    new_quantity = request.POST.get('quantity')
    if new_quantity and new_quantity.isdigit() and int(new_quantity) > 0:
        basket_item.quantity = int(new_quantity)
        basket_item.save()
    
    return redirect('basket_view')

def remove_from_basket(request, item_id):
    if not request.user.is_authenticated:
        return redirect('login')  

    basket_item = get_object_or_404(Basket, id=item_id, user=request.user)
    basket_item.delete()  

    return redirect('basket_view')  

@login_required
def basket_view(request):
    if not request.user.is_authenticated:
        return redirect('login')  
    
    if not request.user.groups.filter(name='user').exists():
        return redirect('account')

    basket_items = Basket.objects.filter(user=request.user)
    total_price = sum(item.total_price() for item in basket_items)

    return render(request, 'basket.html', {
        'basket_items': basket_items,
        'total_price': total_price,
    })