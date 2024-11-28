from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm
from transaction.models import Transaction

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
    # Fetch all transactions related to the user
    transactions = Transaction.objects.filter(user=user)

    return render(request, 'dashboard.html', {
        'transactions': transactions  
    })