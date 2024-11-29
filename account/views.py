from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm
from transaction.models import Transaction
from products.models import Product
from django.core.paginator import Paginator

def account(request):
    return render(request, 'account.html')

def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) 
            return redirect('account')
    else:
        form = RegistrationForm()
    return render(request, 'signup.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'signin.html'
    
    from django.shortcuts import render

@login_required
def dashboard(request):
    user = request.user
    transactions = Transaction.objects.filter(user=user)
    return render(request, 'dashboard.html', {
        'transactions': transactions  
    })
    
@login_required
def dashboard_admin(request):
    products = Product.objects.all()
    return render(request, 'dashboard_admin.html', {
        'products': products
    })
    
@login_required
def dashboard_courier(request):
    transaction = Transaction.objects.all().order_by('-date')
    paginator = Paginator(transaction, 10)  
    page_number = request.GET.get('page')  
    page_obj = paginator.get_page(page_number)
    return render(request, 'dashboard_courier.html', {
        'page_obj': page_obj
    })