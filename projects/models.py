from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    date_completed = models.DateField()
    main_photo = models.ImageField(upload_to='projects/')

    def __str__(self):
        return self.name
