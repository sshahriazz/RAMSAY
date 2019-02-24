from django.urls import path
from accounts import views

app_name = 'accounts'

urlpatterns = [
    path('register/', views.user_register_view, name='register'),
    path('login/', views.user_login_view, name='login'),
    path('logout/', views.user_logout_view, name='logout'),
    path('profile/', views.user_profile_view, name='profile'),
    path('editprofile/', views.edit_profile_view, name='edit_profile'),
    path('changepassword/', views.change_password_view, name='change_password'),
]
