from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('MainSite.urls')),  # This includes MainSite's URLs
    path("contact-us/", include("contact.urls")),
]