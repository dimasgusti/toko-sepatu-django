from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now
from .models import Transaction
from products.models import Basket


@login_required
def checkout(request):
    user = request.user
    print(f"Checking baskets for user: {user.username}")  

    
    baskets = Basket.objects.filter(user=user)
    print(f"Baskets: {baskets}")  

    if not baskets:
        return render(
            request,
            "transaction/checkout.html",
            {"message": "Your basket is empty. Please add items to the basket."},
        )

    
    total_price = sum(basket.total_price() for basket in baskets)

    print(
        f"Total price calculated: Rp {total_price}"
    )  

    if request.method == "POST":
        payment_method = request.POST.get("payment_method", "credit_card")

        
        transaction = Transaction.objects.create(
            user=user,
            total=total_price,
            date=now(),
            status="purchased",
            payment_method=payment_method,
        )
        
        baskets.update(transaction=transaction)
        
        for basket in baskets:
            basket.product.stock -= basket.quantity
            basket.product.save()
            basket.delete()  

        return redirect("transaction_success", transaction_id=transaction.id)

    return render(
        request,
        "transaction/checkout.html",
        {"basket_items": baskets, "total_price": total_price},
    )


def transaction_detail(request, transaction_id):
    transaction = Transaction.objects.get(id=transaction_id)
    return render(request, "transaction/detail.html", {"transaction": transaction})


@login_required
def transaction_success(request, transaction_id):
    transaction = Transaction.objects.get(id=transaction_id, user=request.user)
    return render(request, "transaction/success.html", {"transaction": transaction})

@login_required
def update_transaction_status(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    if request.method == 'POST':
        status = request.POST.get('status')
        if status in ['purchased', 'ondeliver', 'done']:
            transaction.status = status
            transaction.save()
    return redirect('dashboard_courier')
