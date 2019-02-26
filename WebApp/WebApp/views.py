from django.shortcuts import render


def landing_page(request):
    i = 10
    return render(request, 'WebApp/Landing_Page.html', {'page_title': 'Landing Page', 'i': i})
