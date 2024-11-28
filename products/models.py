from django.db import models
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    COLORS = [
        ('Red', 'Red'),
        ('Blue', 'Blue'),
        ('Green', 'Green'),
        ('Black', 'Black'),
        ('White', 'White'),
        ('Other', 'Other')
    ]
    SIZES = [
        ('36', 'EU 36'),
        ('37', 'EU 37'),
        ('38', 'EU 38'),
        ('39', 'EU 39'),
        ('40', 'EU 40'),
        ('41', 'EU 41'),
        ('42', 'EU 42'),
        ('43', 'EU 43'),
        ('44', 'EU 44'),
        ('45', 'EU 45'),
        ('46', 'EU 46'),
        ('47', 'EU 47'),
    ]
    name = models.CharField(max_length=64)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='products',
        null=True,
        blank=True
    )
    color = models.CharField(
        max_length=16,
        choices=COLORS,
        null=True,
        blank=True
    )
    size = models.CharField(
        max_length=3,
        choices=SIZES,
        null=True,
        blank=True
    )
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.name


class Basket(models.Model):
    user = models.ForeignKey('account.User', on_delete=models.CASCADE, related_name='baskets')
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE, related_name='in_baskets')
    transaction = models.ForeignKey('transaction.Transaction', on_delete=models.SET_NULL, null=True, blank=True, related_name='baskets')
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ('user', 'product')

    def __str__(self):
        return f"{self.user.username}'s Basket - {self.product.name} x {self.quantity}"

    # Add the total_price method
    def total_price(self):
        return self.product.price * self.quantity