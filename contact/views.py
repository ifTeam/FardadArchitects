from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .forms import ContactForm

def contact_view(request):
    form = ContactForm()

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process form data (send email, save to DB, etc.)
            messages.success(request, "Your message has been sent successfully!")
            form = ContactForm()  # Reset form after submission
    else:
        form = ContactForm()

    return render(request, "contact.html", {"form": form})
