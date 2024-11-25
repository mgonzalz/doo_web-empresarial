from django.urls import path
from . import views

# URL configuration for webempresa project (pages application).
urlpatterns = [
    path('<int:page_id>/<slug:page_slug>/', views.page, name="sample"),
]
