from django.urls import path, include
from .views import food_category_view, food_ifo_form_category

app_name = 'food'

urlpatterns = [
    path('foodcategory/', food_category_view, name='category'),
    path('foodcategory/<str:category_name>/', food_ifo_form_category, name='category_to_info')
]
