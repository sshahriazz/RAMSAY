from django.shortcuts import render
from accounts.models import Profile
from food.models import FoodCategory, FoodInformation


def landing_page(request):
    user_profile_objects = Profile.objects.all()
    food_information_obj = FoodInformation.objects.all()

    for profile_obj in user_profile_objects:
        for food_info_obj in food_information_obj:
            if food_info_obj.food_category == profile_obj.favourite_category:
                food = FoodInformation.objects.filter(food_category=profile_obj.favourite_category)
                context = {
                    'page_title': "Home",
                    'food': food
                }
                return render(request, 'WebApp/Landing_Page.html', context)

    context = {
        'page_title': "Home"
    }

    return render(request, 'WebApp/Landing_Page.html', context)
