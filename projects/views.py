# projects/views.py
import os
from django.conf import settings
from django.shortcuts import render

def projects_view(request):
    projects_dir = os.path.join(settings.STATIC_ROOT, 'images', 'projects')
    projects = []
    
    # Get all project folders
    for folder in os.listdir(projects_dir):
        if os.path.isdir(os.path.join(projects_dir, folder)):
            # Extract project name from folder name (remove number prefix)
            project_name = ' '.join(folder.split('-')[1:])
            project_data = {
                'name': project_name,
                'folder': folder,
                'image': f'images/projects/{folder}/main.jpg',
                'date': '2000'  # Default date
            }
            projects.append(project_data)
    
    # Sort projects by folder number
    projects.sort(key=lambda x: int(x['folder'].split('-')[0]))
    
    context = {'projects': projects}
    return render(request, 'projects/projects.html', context)