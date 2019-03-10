from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from food.models import FoodCategory


# models for user profile
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='de_pro.jpg', upload_to='profile_pics')
    favourite_category = models.ForeignKey(FoodCategory, on_delete=models.SET_NULL, null=True)
    house = models.CharField(max_length=150, null=True)
    street = models.CharField(max_length=150, null=True)
    area = models.CharField(max_length=150, null=True)
    country = models.CharField(max_length=150, null=True)
    city = models.CharField(max_length=150, null=True)
    country_code = models.CharField(max_length=3, default='+88', null=True)
    phone_number = models.CharField(max_length=11, null=True)

    def __str__(self):
        return f'{self.user.username} Profile'  # f string which return texts and support jinja

    # resizing photo by overriding save() method from django ORM

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        super().save()
        img = Image.open(self.image.path)  # opened current image instance
        # resizing
        if img.height > 600 or img.width > 600:
            output_size = (600, 600)
            img.thumbnail(output_size)
            img.save(self.image.path)
