from multiprocessing import context
import multiprocessing
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
        "DuyuruMesaj": DuyuruModel.objects.get(id=1)
    }
    metin=request.POST.get('mesaj',False)
    if metin:
        speech=gTTS(text=metin,lang='tr', slow=False)
        speech.save("duyuru.mp3")
        playsound("duyuru.mp3")
    return render(request,'pages/duyuru.html',data)

def ogrencizilical(request):
    playsound("static/muzik/Ses/muzik1.mp3")
    return render(request,'pages/hemencal.html')
    
def durdur(request):
    playsound("static/muzik/Ses/muzik1.mp3")
    return render(request,'pages/hemencal.html')

def ogretmenzilical(request):
    playsound("static/muzik/Ses/muzik2.mp3")
    return render(request,'pages/hemencal.html')

def cikiszili(request):
    playsound("static/muzik/Ses/muzik3.mp3")
    return render(request,'pages/hemencal.html')

def istiklalmarsi(request):
    playsound("static/muzik/Resmi/istiklalmarsi.mp3")
    return render(request,'pages/hemencal.html')

def saygidurusu1(request):
    playsound("static/muzik/Resmi/saygi1dakika-istiklalmarsi.mp3")
    return render(request,'pages/hemencal.html')

def saygidurusu2(request):
    playsound("static/muzik/Resmi/saygi2dakika-istiklalmarsi.mp3")
    return render(request,'pages/hemencal.html')

def siren(request):
    playsound("static/muzik/Resmi/siren30saniye.mp3")
    return render(request,'pages/hemencal.html')