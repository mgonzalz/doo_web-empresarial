from django.urls import path
from . import views

# URL configuration for webempresa project (core application).
urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('store/', views.store, name="store"),
]
