# Helps to set profile by default.
from django.db.models.signals import post_save
# gets fired when a db or form updates
from django.contrib.auth.models import User
from django.dispatch import receiver
# signal Receiver
from .models import Profile


# its a activity listner for a user to create automatic profile and updating profile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

# adding default_app_config = 'users.apps.UsersConfig' is necessary to the _init_.py file.
