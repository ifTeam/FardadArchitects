import os
from django.conf import settings
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
    """ Display a single project's details with multiple galleries """
    project_dir = os.path.join(settings.BASE_DIR, "static", "images", "projects", project_id)
    info_path = os.path.join(project_dir, "info.txt")

    if not os.path.exists(info_path):
        return render(request, "404.html")  # Error handling

    # Read info.txt
    project_info = {}
    with open(info_path, "r", encoding="utf-8") as file:
        for line in file:
            if ":" in line:
                key, value = line.split(":", 1)
                project_info[key.strip().lower()] = value.strip()
            else:
                project_info["status"] = line.strip()

    # Check if images exist, fallback to main.jpg if not found
    main_image = f"images/projects/{project_id}/main.jpg"
    day_image = main_image if not os.path.exists(os.path.join(project_dir, "day.jpg")) else f"images/projects/{project_id}/day.jpg"
    night_image = main_image if not os.path.exists(os.path.join(project_dir, "night.jpg")) else f"images/projects/{project_id}/night.jpg"

    # Add the map.svg path
    map_svg = f"images/projects/{project_id}/map.svg"

    # Get main slideshow images (images in root folder)
    main_slideshow = sorted([
        f for f in os.listdir(project_dir) if f.endswith((".jpg", ".png")) and f[:2].isdigit()
    ])

    # Collect sub-gallery images
    sub_galleries = {}
    for folder in sorted(os.listdir(project_dir)):
        subdir_path = os.path.join(project_dir, folder)
        if os.path.isdir(subdir_path) and folder.lower().startswith("no"):  # Check if it's a sub-gallery
            images = sorted([
                f for f in os.listdir(subdir_path) if f.endswith((".jpg", ".png"))
            ])
            if images:
                sub_galleries[folder] = [f"images/projects/{project_id}/{folder}/{img}" for img in images]

    # Prepare slideshows data
    slideshows = {
        "Main Slideshow": [f"images/projects/{project_id}/{img}" for img in main_slideshow]
    }
    slideshows.update(sub_galleries)  # Add sub-gallery slideshows

    context = {
        "project": {
            "id": project_id,
            "name": project_info.get("name", "Unknown").upper(),
            "date": project_info.get("date", "Unknown"),
            "location": project_info.get("location", "Unknown"),
            "client": project_info.get("client", "Unknown"),
            "constructor": project_info.get("constructor", "Unknown"),
            "area": project_info.get("area", "Unknown"),
            "status": project_info.get("status", ""),
            "day_image": day_image,
            "night_image": night_image,
            "map_svg": map_svg,
            "slideshows": slideshows,
        }
    }

    return render(request, "projects/project_detail.html", context)
