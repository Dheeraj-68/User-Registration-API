#signals.py

from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from .models import Profile

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile, _ = Profile.objects.get_or_create(user=instance)
        profile.profile_first_name = instance.first_name
        profile.profile_last_name = instance.last_name
        profile.email = instance.email
        profile.save()