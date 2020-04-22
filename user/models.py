from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    prof_pic = models.ImageField(default="default.jpg", upload_to='profile_pics')
    bio = models.TextField()
    address = models.CharField(max_length=100)
    date_joined = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username}'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.prof_pic.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.prof_pic.path)
