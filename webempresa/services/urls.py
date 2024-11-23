from django.urls import path
from . import views

# URL configuration for webempresa project (services application).
urlpatterns = [
    path('', views.services, name="services"),
]
