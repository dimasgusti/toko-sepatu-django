from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('create/', views.create_product, name='create_product'),
    path('basket/', views.basket_view, name='basket_view'),
    path('wishlist/', views.wishlist_view, name='wishlist_view'),
    path('add-to-basket/<int:product_id>/', views.add_to_basket, name='add_to_basket'),
    path('add-to-wishlist/<int:product_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('remove-from-basket/<int:item_id>/', views.remove_from_basket, name='remove_from_basket'),
    path('remove-from-wishlist/<int:item_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),
]
