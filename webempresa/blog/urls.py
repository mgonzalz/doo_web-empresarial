from django.urls import path
from . import views

# URL configuration for webempresa project (blog application).
urlpatterns = [
    path('', views.blog, name="blog"),
]
