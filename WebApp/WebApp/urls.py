from django.contrib import admin
from django.urls import path, include
from .views import landing_page, search_view
from django.conf import settings
from django.conf.urls.static import static

app_name = 'WebApp'

urlpatterns = [
    path('', landing_page, name="landing_page"),
    path('admin/', admin.site.urls, name="admin"),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('food/', include('food.urls', namespace='food')),
    path('search/', search_view, name='search')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
