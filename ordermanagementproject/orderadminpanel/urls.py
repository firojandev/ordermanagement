from django.urls import path

from . import views as adminpanel

urlpatterns = [
    path('', adminpanel.home),
]