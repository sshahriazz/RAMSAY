from django.urls import path, include
from .views import food_category_view, all_food_view, food_ifo_form_category, food_details_bosc

app_name = 'food'

urlpatterns = [
    path('foodcategory/', food_category_view, name='category'),
    path('foodcategory/<str:category_name>/', food_ifo_form_category, name='category_to_info'),
    path('fooddetails/<str:food_name>/', food_details_bosc, name='food_details'),
    path('foodlists/', all_food_view, name='all_foods')
]
