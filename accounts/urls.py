from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='accounts-register'),
    path('login/', views.login_request, name='accounts-login'),
    path('logout/', views.logout_request, name='accounts-logout'),
]
