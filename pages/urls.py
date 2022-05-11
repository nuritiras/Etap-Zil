from django.urls import path
from . import views

# http://127.0.0.1:8000/

urlpatterns = [
    path('', views.index, name='index'),
    path('hemencal', views.hemencal, name='hemencal'),
    path('saatler', views.saatler, name='saatler'), 
    path('meolodiler', views.melodiler, name='melodiler'),
    path('duyuru', views.duyuru, name='duyuru'),
    path('duyuru/<int:id>', views.duyurudetails, name='details'),
    path('ogrencizilical', views.ogrencizilical, name='ogrencizilical'),
    path('ogretmenzilical', views.ogretmenzilical, name='ogretmenzilical'),
    path('cikiszili', views.cikiszili, name='cikiszili'),
    path('istiklalmarsi', views.istiklalmarsi, name='istiklalmarsi'),
    path('saygidurusu1', views.saygidurusu1, name='saygidurusu1'),
    path('saygidurusu2', views.saygidurusu2, name='saygidurusu2'),
    path('siren', views.siren, name='siren'),
    path('durdur', views.durdur, name='durdur'),
]