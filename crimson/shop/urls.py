from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "shop-index"),
    path('about/', views.about, name = "shop-about"),
]