from django.db import models

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
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'X-Large'),
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
        max_length=2,
        choices=SIZES,
        null=True,
        blank=True
    )
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    
    def __str__(self):
        return self.name
    
class Wishlist(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='wishlists')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='wishlisted_by')
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'product')  # Prevent duplicate entries

    def __str__(self):
        return f"{self.user.username}'s Wishlist - {self.product.name}"
    
class Basket(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='baskets')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='in_baskets')
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'product')  # Prevent duplicate entries

    def __str__(self):
        return f"{self.user.username}'s Basket - {self.product.name} x {self.quantity}"