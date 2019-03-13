from django.shortcuts import render
from food.models import FoodInformation, FoodCategory


# Create your views here.

def food_category_view(request):
    category = FoodCategory.objects.all()
    context = {
        'page_title': 'Food Category\'s',
        'category': category
    }
    return render(request, 'food/food_category.html', context)


def food_ifo_form_category(request, category_name):
    lists = FoodInformation.objects.filter(food_category__category_name=category_name)
    context = {
        'list': lists,
        'page_title': f'Details/{category_name}'
    }

    return render(request, 'food/food_details_boc.html', context)


def food_details_bosc(request, food_name):
    food_detail = FoodInformation.objects.filter(food_name__exact=food_name)
    return render(request, 'food/food_details.html', {'food': food_detail})


def all_food_view(request):
    food_detail = FoodInformation.objects.all()
    return render(request, 'food/all_food.html', {'food': food_detail})
