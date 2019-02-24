from django.shortcuts import render


def landing_page(request):
    return render(request, 'WebApp/Landing_Page.html', {'page_title': 'Landing Page'})
