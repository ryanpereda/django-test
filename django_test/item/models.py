from django.db import models

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=255)
    link = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name