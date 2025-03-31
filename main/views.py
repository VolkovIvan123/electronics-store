from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'main/home.html')

def catalog(request):
    return render(request, 'main/catalog.html')

def about(request):
    return render(request, 'main/about.html')

def contacts(request):
    return render(request, 'main/contacts.html')

def pinterest(request):
    return render(request, 'main/pinterest.html')
