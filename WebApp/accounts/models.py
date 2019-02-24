from django.db import models
from django.contrib.auth.models import User
from PIL import Image


# models for user profile
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='de_pro.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile' # f string which return texts and support jinja

    # resizing photo by overriding save() method from django ORM

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        super().save()
        img = Image.open(self.image.path)  # opened current image instance
        # resizing
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
