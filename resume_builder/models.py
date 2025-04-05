from django.db import models

# Create your models here.

class ResumeTemplate(models.Model):
    name = models.CharField(max_length=100)  # Template Name
    description = models.TextField()  # Short Description
    image = models.ImageField(upload_to="resume_templates/")  # Preview Image
    template_url = models.CharField(max_length=255)  # URL to editor page

    def __str__(self):
        return self.name
