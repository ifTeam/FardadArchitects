from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .forms import ContactForm

def contact_view(request):
    form = ContactForm()

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            subject = form.cleaned_data["subject"]
            message = form.cleaned_data["message"]

            # Send email (Make sure you have email settings configured)
            send_mail(
                f"New Contact Form Submission: {subject}",
                f"From: {name} ({email})\n\n{message}",
                "your-email@example.com",  # Change to your email
                ["your-email@example.com"],  # Recipient email
                fail_silently=False,
            )

            messages.success(request, "Your message has been sent!")
            return redirect("contact")  # Redirect back to the form after submission

    return render(request, "contact/contact.html", {"form": form})
