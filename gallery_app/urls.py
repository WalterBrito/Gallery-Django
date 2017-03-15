from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^photos/', views.photos, name='photos'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^about/', views.about, name='about'),
]
