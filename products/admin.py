from django.contrib import admin
from .models import Product, Category, Basket, Wishlist

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'stock']
    raw_id_fields = ['category']  # This will show the category as an ID field instead of a dropdown.

admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Basket)
admin.site.register(Wishlist)