from django.urls import path
from . import views

urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
    path('success/<int:transaction_id>/', views.transaction_success, name='transaction_success'),
    path('transaction/<int:transaction_id>/', views.transaction_detail, name='transaction_detail'),
    path('transaction/update/<int:pk>/', views.update_transaction_status, name='update_transaction_status'),
]
