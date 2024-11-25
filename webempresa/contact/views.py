from django.shortcuts import render, redirect
from .forms import ContactForm

# Create your views here.
def contact(request):
    contact_form = ContactForm()
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
    if contact_form.is_valid():
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        content = request.POST.get('content', '')
        # Suponemos que el envío de correo es correcto, si el campo no está presente, se envía una cadena vacía.
    return render(request, "contact/contact.html", {'form': contact_form})
