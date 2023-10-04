from django.urls import path

from . import views as orderapi

urlpatterns = [
    path('', orderapi.welcome),
]