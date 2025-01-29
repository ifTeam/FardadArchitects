from django.shortcuts import render

def home(request):
    return render(request, 'home.html')  # No need for app-specific subfolders
