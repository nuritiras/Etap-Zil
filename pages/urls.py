from django.urls import path
from . import views

# http://127.0.0.1:8000/

urlpatterns = [
    path('', views.index, name='index'),
    path('hemencal', views.hemencal, name='hemencal'),
    path('saatler', views.saatler, name='saatler'), 
    path('meolodiler', views.melodiler, name='melodiler'),
    path('duyuru', views.duyuru, name='duyuru'),
]