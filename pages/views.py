from multiprocessing import context
import multiprocessing
from django.shortcuts import render
from django.http import HttpResponse
from okulzili.models import DuyuruModel
from gtts import gTTS
from pygame import mixer

mixer.init()

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
        "DuyuruMesaj": DuyuruModel.objects.all()
    }
    return render(request,'pages/duyuru.html',data)

def duyurudetails(request, id):
    data = {
        "DuyuruMesaj": DuyuruModel.objects.get(id=id)
    }
    metin=request.POST.get('mesaj',False)
    if metin:
        speech=gTTS(text=metin,lang='tr', slow=False)
        speech.save("duyuru.mp3")
        mixer.music.load("duyuru.mp3") 
        mixer.music.set_volume(0.1)
        mixer.music.play()
        
    return render(request, "details.html", data)

def ogrencizilical(request):
    mixer.music.load("static/muzik/Ses/muzik1.mp3") 
    mixer.music.set_volume(0.1)
    mixer.music.play()
    return render(request,'pages/hemencal.html')
    
def durdur(request):
    mixer.music.stop()
    return render(request,'pages/hemencal.html')

def ogretmenzilical(request):
    mixer.music.load("static/muzik/Ses/muzik2.mp3") 
    mixer.music.set_volume(0.1)
    mixer.music.play()
    return render(request,'pages/hemencal.html')

def cikiszili(request):
    mixer.music.load("static/muzik/Ses/muzik3.mp3") 
    mixer.music.set_volume(0.1)
    mixer.music.play()
    return render(request,'pages/hemencal.html')

def istiklalmarsi(request):
    mixer.music.load("static/muzik/Resmi/istiklalmarsi.mp3") 
    mixer.music.set_volume(0.1)
    mixer.music.play()
    return render(request,'pages/hemencal.html')

def saygidurusu1(request):
    mixer.music.load("static/muzik/Resmi/saygi1dakika-istiklalmarsi.mp3") 
    mixer.music.set_volume(0.1)
    mixer.music.play()
    return render(request,'pages/hemencal.html')

def saygidurusu2(request):
    mixer.music.load("static/muzik/Resmi/saygi2dakika-istiklalmarsi.mp3") 
    mixer.music.set_volume(0.1)
    mixer.music.play()
    return render(request,'pages/hemencal.html')

def siren(request):
    mixer.music.load("static/muzik/Resmi/siren30saniye.mp3") 
    mixer.music.set_volume(0.1)
    mixer.music.play()
    return render(request,'pages/hemencal.html')