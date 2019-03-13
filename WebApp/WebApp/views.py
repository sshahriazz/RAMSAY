from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from accounts.models import Profile
from food.models import FoodInformation, FoodCategory


def landing_page(request):
    user_profile_objects = Profile.objects.all()
    food_information_obj = FoodInformation.objects.all()
    if User.is_authenticated:
        for profile_obj in user_profile_objects:
            for food_info_obj in food_information_obj:
                if food_info_obj.food_category == profile_obj.favourite_category:
                    food = FoodInformation.objects.filter(food_category=profile_obj.favourite_category)
                    context = {
                        'page_title': "Home",
                        'food': food,
                        'food_info': food_information_obj
                    }
                    return render(request, 'WebApp/Landing_Page.html', context)
    else:
        return render(request, 'WebApp/Landing_Page.html', {'page_title': "Home",
                                                            'food_info': food_information_obj})


def search_view(request):
    if request.method == "GET":
        search_query = request.GET.get('search_tag')
        search_tag = FoodInformation.objects.filter(
            food_name__contains=search_query) or FoodInformation.objects.filter(
            food_category__category_name__contains=search_query) or FoodInformation.objects.filter(
            food_short_info__contains=search_query)
        return render(request, 'WebApp/search.html', {'search': search_tag})
