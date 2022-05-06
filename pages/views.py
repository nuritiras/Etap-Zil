from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from okulzili.models import okulzili

def index(request):
    okulzilis = okulzili.objects.all()

# Create your views here.
# http://127.0.0.1:8000/

def index(request):
    return render(request,'pages/index.html')

def hemencal(request):
    return render(request,'pages/hemencal.html')

def saatler(request):
    return render(request,'pages/saatler.html')

def melodiler(request):
    return render(request,'pages/melodiler.html')

def duyuru(request):
    return render(request,'pages/duyuru.html')