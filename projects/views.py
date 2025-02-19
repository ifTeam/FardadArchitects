import os
from django.conf import settings
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404

def read_info_file(info_path):
    """ Read info.txt and return a dictionary of its contents """
    info_data = {}
    print(f"Reading file: {info_path}")  # Debugging line

    if os.path.exists(info_path):
        with open(info_path, "r", encoding="utf-8") as file:
            for line in file:
                print(f"Line read: {line.strip()}")  # Debugging line
                if ":" in line:
                    key, value = line.split(":", 1)
                    info_data[key.strip().lower()] = value.strip()
                else:
                    info_data["status"] = line.strip()  # Last line without a key

    print(f"Parsed data: {info_data}")  # Debugging line
    return info_data


def projects_view(request):
    projects_dir = os.path.join(settings.BASE_DIR, "static", "images", "projects")
    projects = []

    for folder in os.listdir(projects_dir):
        folder_path = os.path.join(projects_dir, folder)
        if os.path.isdir(folder_path):
            info_path = os.path.join(folder_path, "info.txt")
            info = read_info_file(info_path)

            project_data = {
                "id": folder,  # Using folder name as a unique ID
                "name": info.get("name", "Unknown"),
                "date": info.get("date", "Unknown"),
                "location": info.get("location", "Unknown"),
                "client": info.get("client", "Unknown"),
                "constructor": info.get("constructor", "Unknown"),
                "area": info.get("area", "Unknown"),
                "status": info.get("status", ""),
                "image": f"images/projects/{folder}/main.jpg",
            }
            projects.append(project_data)

    projects.sort(key=lambda x: int(x["id"].split("-")[0]))  # Sort by number prefix

    return render(request, "projects/projects.html", {"projects": projects})


def project_detail_view(request, project_id):
    """ Display a single project's details """
    project_dir = os.path.join(settings.STATIC_ROOT, "images", "projects", project_id)
    info_path = os.path.join(project_dir, "info.txt")

    if not os.path.exists(info_path):
        return render(request, "404.html")  # Handle missing projects gracefully

    project_info = read_info_file(info_path)

    # Get all images for the slideshow
    image_files = sorted([
        f for f in os.listdir(project_dir)
        if f.endswith((".jpg", ".png")) and f[:2].isdigit()  # Images like 01.jpg, 02.jpg
    ])

    context = {
        "project": {
            "id": project_id,
            "name": project_info.get("name", "Unknown"),
            "date": project_info.get("date", "Unknown"),
            "location": project_info.get("location", "Unknown"),
            "client": project_info.get("client", "Unknown"),
            "constructor": project_info.get("constructor", "Unknown"),
            "area": project_info.get("area", "Unknown"),
            "status": project_info.get("status", ""),
            "day_image": f"images/projects/{project_id}/day.jpg",
            "night_image": f"images/projects/{project_id}/night.jpg",
            "slideshow_images": [f"images/projects/{project_id}/{img}" for img in image_files],
        }
    }
    
    return render(request, "projects/project_detail.html", context)
