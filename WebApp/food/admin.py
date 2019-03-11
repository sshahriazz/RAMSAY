from django.contrib import admin
from .models import FoodCategory, FoodInformation
# Register your models here.
admin.site.register(FoodCategory)
admin.site.register(FoodInformation)

