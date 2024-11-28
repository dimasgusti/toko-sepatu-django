from django.db import models
from account.models import User

class Transaction(models.Model):
    STATUS_CHOICES = [
        ('purchased', 'Purchased'),
        ('ondeliver', 'On Deliver'),
        ('success', 'Success'),
    ]
    PAYMENT_METHOD_CHOICES = [
        ('credit_card', 'Credit Card'),
        ('bank_transfer', 'Bank Transfer'),
        ('cash', 'Cash'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="transactions", null=True, blank=True)  # Temporarily nullable
    total = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=16, choices=STATUS_CHOICES, default='purchased')
    payment_method = models.CharField(max_length=16, choices=PAYMENT_METHOD_CHOICES)

    def __str__(self):
        return f"Transaction {self.id} by {self.user.username if self.user else 'Unknown User'}"