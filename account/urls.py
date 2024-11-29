from django.urls import path
from . import views
from .views import signup, CustomLoginView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.account, name='account'),
    path('signup/', signup, name='signup'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard_admin/', views.dashboard_admin, name='dashboard_admin'),
    path('dashboard_courier', views.dashboard_courier, name='dashboard_courier'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
