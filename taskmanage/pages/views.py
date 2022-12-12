from django.shortcuts import render


def homePageView(request):
    return render(request, 'home.html')

def aboutPageView(request):
    return render(request, 'about.html')

def servicesPageView(request):
    return render(request, 'services.html')

def contactsPageView(request):
    return render(request, 'contacts.html')

def pricesPageView(request):
    return render(request, 'prices.html')

def productsPageView(request):
    return render(request, 'products.html')


