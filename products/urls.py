from django.urls import path
from . import views
from .views import edit_product, delete_product

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('create/', views.create_product, name='create_product'),
    path('product/edit/<int:pk>/', edit_product, name='edit_product'),
    path('product/delete/<int:pk>/', delete_product, name='delete_product'),
    path('basket/', views.basket_view, name='basket_view'),
    path('add-to-basket/<int:product_id>/', views.add_to_basket, name='add_to_basket'),
    path('delete-from-basket/<int:item_id>/', views.remove_from_basket, name='remove_from_basket'),
    path('update-basket/<int:item_id>/', views.update_basket_item, name='update_basket_item'),
]
