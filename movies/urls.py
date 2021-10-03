from django.urls import path
from . import views
from .views import dash, book
urlpatterns = [
    path('<pk>/', dash.as_view(), name='movies-dash'),
    path('<str:pk>/book/', book, name='movies-book')
]
