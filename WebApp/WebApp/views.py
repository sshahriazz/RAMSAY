from django.contrib.auth.models import User
from django.shortcuts import render
from accounts.models import Profile
from food.models import FoodInformation
from ipware import get_client_ip
import requests
from django.contrib.gis.geoip2 import GeoIP2


def get_city(request):
    ip_data = get_client_ip(request)
    client_ip = ip_data[0]
    geo_data = GeoIP2()
    citys = geo_data.city('103.76.152.246')  # in production this will be replaced by client_ip variable
    extract_city = str(citys['time_zone'])
    splited_data = extract_city.split('/')
    city = splited_data[1]
    return city


def landing_page(request):
    user_profile_objects = Profile.objects.all()
    food_information_obj = FoodInformation.objects.all()

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=271d1234d3f497eed5b1d80a07b3fcd1'

    city = get_city(request)
    print(city)
    city_weather = requests.get(
        url.format(city)).json()  # request the API data and convert the JSON to Python data types
    weather_data = []
    weather = {
        'city': city,
        'temperature': city_weather['main']['temp'],
        'description': city_weather['weather'][0]['description'],
        'icon': city_weather['weather'][0]['icon']
    }

    weather_data.append(weather)  # add the data for the current city into our list

    if User.is_authenticated:
        for profile_obj in user_profile_objects:
            for food_info_obj in food_information_obj:
                if food_info_obj.food_category == profile_obj.favourite_category:
                    food = FoodInformation.objects.filter(food_category=profile_obj.favourite_category)

                    context = {
                        'page_title': "Home",
                        'food': food,
                        'food_info': food_information_obj,
                        'weather_data': weather_data
                    }
                    return render(request, 'WebApp/Landing_Page.html', context)
        else:
            return render(request, 'WebApp/Landing_Page.html', {'page_title': "Home",
                                                                'food_info': food_information_obj,
                                                                'weather_data': weather_data
                                                                })


def search_view(request):
    if request.method == "GET":
        search_query = request.GET.get('search_tag')
        search_tag = FoodInformation.objects.filter(
            food_name__contains=search_query) or FoodInformation.objects.filter(
            food_category__category_name__contains=search_query) or FoodInformation.objects.filter(
            food_short_info__contains=search_query)
        return render(request, 'WebApp/search.html', {'search': search_tag})

# def weather_data_view(request):
#     url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=271d1234d3f497eed5b1d80a07b3fcd1'
#
#     weather_data = []
#     city = get_city(request)
#     print(city)
#     city_weather = requests.get(url.format(city)).json()  # request the API data and convert the JSON to Python data types
#
#     weather = {
#         'city': city,
#         'temperature': city_weather['main']['temp'],
#         'description': city_weather['weather'][0]['description'],
#         'icon': city_weather['weather'][0]['icon']
#     }
#
#     weather_data.append(weather)  # add the data for the current city into our list
#
#     context = {'weather_data': weather_data}
#
#     return render(request, 'WebApp/weathertest.html', context)  # returns the weathertest.html template
