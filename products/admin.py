from django.contrib import admin
from .models import Product, Category, Basket

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'stock']
    raw_id_fields = ['category'] 

admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Basket)