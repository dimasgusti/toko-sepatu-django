from django.db import models

class Transaction(models.Model):
    STATUS_CHOICES = [
        ('purchased', 'Purchased'),
        ('ondeliver', 'On Delivery'),
        ('finished', 'Finished'),
    ]
    
    PAYMENT_METHOD_CHOICES = [
        ('credit_card', 'Credit Card'),
        ('paypal', 'PayPal'),
        ('bank_transfer', 'Bank Transfer'),
        ('cash_on_delivery', 'Cash on Delivery'),
    ]
    
    # user = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='purchased')
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES)

    def __str__(self):
        return f"Transaction #{self.id} - {self.user.username} - {self.status}"