from django.urls import path
from . import views

# URL configuration for webempresa project (contact application).
urlpatterns = [
    path('', views.contact, name="contact"),
]
