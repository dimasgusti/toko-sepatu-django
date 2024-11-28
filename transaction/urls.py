from django.urls import path
from . import views
from .views import transaction_detail, checkout, transaction_success

urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
    path('success/<int:transaction_id>/', views.transaction_success, name='transaction_success'),
    path('transaction/<int:transaction_id>/', views.transaction_detail, name='transaction_detail'),
]
