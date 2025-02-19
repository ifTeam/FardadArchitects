from django.urls import path
from .views import projects_view, project_detail_view

urlpatterns = [
    path("", projects_view, name="projects"),
    path('projects/', projects_view, name='projects'),
    path("<str:project_id>/", project_detail_view, name="project_detail"),
]
