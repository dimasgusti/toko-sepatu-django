from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now
from django.http import HttpResponse
from .models import Transaction
from products.models import Basket


@login_required
def checkout(request):
    user = request.user
    print(f"Checking baskets for user: {user.username}")  # Debugging line to check user

    # Try fetching baskets without transaction filter
    baskets = Basket.objects.filter(user=user)
    print(f"Baskets: {baskets}")  # Debugging line to check basket items

    if not baskets:
        return render(
            request,
            "transaction/checkout.html",
            {"message": "Your basket is empty. Please add items to the basket."},
        )

    # Calculate total price of items in the basket
    total_price = sum(basket.total_price() for basket in baskets)

    print(
        f"Total price calculated: Rp {total_price}"
    )  # Debugging line to check the total price

    if request.method == "POST":
        payment_method = request.POST.get("payment_method", "credit_card")

        # Create the transaction
        transaction = Transaction.objects.create(
            user=user,
            total=total_price,
            date=now(),
            status="purchased",
            payment_method=payment_method,
        )

        # Link baskets to the transaction
        baskets.update(transaction=transaction)

        # Update product stock and clear baskets after purchase
        for basket in baskets:
            basket.product.stock -= basket.quantity
            basket.product.save()
            basket.delete()  # Clear the basket after purchase

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
