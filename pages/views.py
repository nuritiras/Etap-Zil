from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from okulzili.models import DuyuruModel
from gtts import gTTS
from playsound import playsound

def index(request):
    okulzilis = DuyuruModel.objects.all()

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
    data = {
        "DuyuruMesaj": DuyuruModel.objects.get(id=2)
    }
    metin=request.POST.get('mesaj',False)
    if metin:
        speech=gTTS(text=metin,lang='tr', slow=False)
        speech.save("duyuru.mp3")
        playsound("duyuru.mp3")
    return render(request,'pages/duyuru.html',data)