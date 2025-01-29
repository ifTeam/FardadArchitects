from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('projects/', projects, name='projects'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
]
