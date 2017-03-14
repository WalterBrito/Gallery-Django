from django.shortcuts import render

def home(request):
    return render(request, 'gallery_app/home.html', {})
