from django.shortcuts import render

def transaction(request):
    return render(request, 'transaction.html')