from django.shortcuts import render

def home(request):
    return render(request, 'home.html')  # No need for app-specific subfolders

def projects(request):
    return render(request, 'projects.html')

def contact(request):
    return render(request, 'contact.html')

def about_view(request):
    return render(request, 'about.html')