from django.db.models.signals import post_save
from django.contrib.auth.models import User
#from django.dispatch import reciever
from .models import Profile

#Signal.connect(reciever, connect=None, weak=True, dispatch_uid=None)

#@reciever(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance) 


#@reciever(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.Profile.save() 