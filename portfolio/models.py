from django.db import models

# Create your models here.
class Project(models.Model):
    person = models.CharField(max_length=30)
    title = models.CharField(max_length=50)
    description = models.TextField()
    technology = models.CharField(max_length=250)
    image = models.FileField(upload_to='img/')