from django.urls import path
from . import views
from .views import signup, CustomLoginView, dashboard
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.account, name='account'),
    path('signup/', signup, name='signup'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
