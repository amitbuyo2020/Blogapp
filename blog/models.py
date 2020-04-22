from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    date_posted = models.DateTimeField(default=timezone.now)
    content = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Announcements(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    posted_date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.title


class Calendar(models.Model):
    heading = models.DateTimeField(default=timezone.now())
    content = models.TextField()
    location = models.TextField()
    title = models.CharField(max_length=100)


    def __str__(self):
        return self.title
