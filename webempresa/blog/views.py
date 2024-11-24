from django.shortcuts import render, get_object_or_404
from .models import Post, Category

# Create your views here.
def blog(request):
    posts = Post.objects.all()
    return render(request, "blog/blog.html", {'posts':posts})

def category(request, category_id):
    category = get_object_or_404(Category, id=category_id) # si no existe la categoría, se mostrará un error 404
    return render(request, "blog/category.html", {'category':category}) # poner en la dirección: /category/1/ siendo 1 el ID de la categoría
