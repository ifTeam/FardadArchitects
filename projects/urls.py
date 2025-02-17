from django.urls import path
from .views import projects_view

urlpatterns = [
    path('projects/', projects_view, name='projects'),
]