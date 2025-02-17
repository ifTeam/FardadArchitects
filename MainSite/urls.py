from django.urls import path,include
from .views import *  # Assuming you have the views for 'home', 'contact', 'about', etc.

urlpatterns = [
    path('', home, name='home'),
    path('projects/', include('projects.urls')),  # This includes the URLs of the projects app
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
]
