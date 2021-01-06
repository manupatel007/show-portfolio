from django.db import models
from django.conf import settings

# Create your models here.
class Project(models.Model):
    person = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=50)
    description = models.TextField()
    technology = models.CharField(max_length=250)
    main_image = models.FileField(upload_to='img/')
    source_code = models.CharField(max_length=50)
    img1 = models.FileField(upload_to='img/')
    img2 = models.FileField(upload_to='img/')
    img3 = models.FileField(upload_to='img/')



class NewFields(models.Model):
    person = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    profile_pic = models.FileField(upload_to='img/')
    skills = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    contact = models.CharField(max_length=50)
    bio = models.TextField()


class FollowersField(models.Model):
    person = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    followers = models.CharField(max_length=50)

class FollowingField(models.Model):
    person = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    following = models.CharField(max_length=50)

class NotificationsField(models.Model):
    person = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    notifications = models.CharField(max_length=200)


