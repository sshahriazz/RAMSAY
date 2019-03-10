from django.contrib.auth.models import User
from django.db import models
from PIL import Image


class FoodCategory(models.Model):
    category_name = models.CharField(max_length=50, null=False)
    category_image = models.ImageField(default='default_food.jpg', upload_to='food_cat_images')
    category_short_description = models.CharField(max_length=250)
    category_long_description = models.CharField(max_length=500)

    def __str__(self):
        return self.category_name

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        super().save()
        img = Image.open(self.category_image.path)  # opened current image instance
        # resizing
        if img.height > 600 or img.width > 600:
            output_size = (600, 600)
            img.thumbnail(output_size)
            img.save(self.category_image.path)


class FoodInformation(models.Model):
    food_category = models.ForeignKey(FoodCategory, on_delete=models.CASCADE)
    food_name = models.CharField(max_length=50)
    food_image = models.ImageField(default='default_food.jpg', upload_to='food_cat_images')
    food_short_info = models.CharField(max_length=250)
    food_long_description = models.CharField(max_length=500)
    food_love = models.IntegerField(null=True)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    upload_date = models.DateTimeField(auto_now_add=True, blank=False)

    def __str__(self):
        return self.food_name + " - From - " + self.food_category.category_name + " Category"

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        super().save()
        img = Image.open(self.food_image.path)  # opened current image instance
        # resizing
        if img.height > 600 or img.width > 600:
            output_size = (600, 600)
            img.thumbnail(output_size)
            img.save(self.food_image.path)
