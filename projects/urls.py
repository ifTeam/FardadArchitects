from django.urls import path
from . import views

urlpatterns = [
    path('', views.project_gallery, name='projects'),  # Change 'project_gallery' to 'projects'
    path('<int:project_id>/', views.project_detail, name='project_detail'),  # Keep the detail URL
]
