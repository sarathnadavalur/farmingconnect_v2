
from django.urls import path
from . import views

urlpatterns = [
    path('', views.retailers, name='retailers'),
]
