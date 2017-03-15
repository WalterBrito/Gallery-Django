from django.shortcuts import render

def home(request):
    return render(request, 'gallery_app/home.html', {})

def photos(request):
    return render(request, 'gallery_app/photos.html', {})

def contact(request):
    return render(request, 'gallery_app/contact.html', {})

def about(request):
    return render(request, 'gallery_app/about.html', {})
