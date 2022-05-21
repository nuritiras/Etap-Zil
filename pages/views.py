from multiprocessing import context
import multiprocessing
from django.shortcuts import render
from django.http import HttpResponse
from okulzili.models import DuyuruModel,SaatModel,OgrenciMelodiModel,OgretmenMelodiModel,CikisMelodiModel
from gtts import gTTS
from pygame import mixer
from django.contrib import messages

mixer.init()
sesseviyesi=50

def index(request):
    okulzilis = DuyuruModel.objects.all()

# Create your views here.
# http://127.0.0.1:8000/

def index(request):
    if request.method == 'POST':
        sesseviyesi=request.POST['sesseviyesi']
    return render(request,'pages/index.html')

def hemencal(request):
    return render(request,'pages/hemencal.html')

def saatler(request):
    data = {
        "girisCikisSaatleri": SaatModel.objects.all()
    }
    
    if request.method == 'POST':
        ogrenciDersZili={}
        ogretmenDersZili={}
        cikisDersZili={}
        sesSeviyesi={}
        for i in range(1,22):
            ogrenciDersZili[i] = request.POST['ogrenci'+str(i)]
            ogretmenDersZili[i] = request.POST['ogretmen'+str(i)]
            cikisDersZili[i] = request.POST['cikis'+str(i)]
            sesSeviyesi[i]=request.POST['sesseviyesi'+str(i)]
            SaatModel.objects.filter(id=i).update(ogrenci=ogrenciDersZili[i],ogretmen=ogretmenDersZili[i],cikis=cikisDersZili[i],sesDuzeyi=sesSeviyesi[i])
        messages.add_message(request, messages.SUCCESS, 'Giriş-çıkış ders saatleri ayarlandı.')    
    return render(request, 'pages/saatler.html',data)

def melodiler(request):
    return render(request,'pages/melodiler.html')

def duyuru(request):
    data = {
        "DuyuruMesaj": DuyuruModel.objects.all()
    }
    return render(request,'pages/duyuru.html',data)

def duyurudetails(request, id):
    if request.method == 'POST':
        sesseviyesi=request.POST['sesseviyesi']
        metin=request.POST.get('mesaj',False)
        if metin:
            speech=gTTS(text=metin,lang='tr', slow=False)
            speech.save("duyuru.mp3")
            mixer.music.load("duyuru.mp3") 
            mixer.music.set_volume(int(sesseviyesi)/100)
            mixer.music.play()
            DuyuruModel.objects.filter(id=id).update(description=metin)
    data = {
        "DuyuruMesaj": DuyuruModel.objects.get(id=id)
    }
    return render(request, "pages/details.html", data)

def ogrencizilical(request):
    mixer.music.load("static/muzik/Ses/muzik1.mp3") 
    mixer.music.set_volume(sesseviyesi/100)
    mixer.music.play()
    return render(request,'pages/hemencal.html')
    
def durdur(request):
    mixer.music.stop()
    return render(request,'pages/hemencal.html')

def ogretmenzilical(request):
    mixer.music.load("static/muzik/Ses/muzik2.mp3") 
    mixer.music.set_volume(sesseviyesi/100)
    mixer.music.play()
    return render(request,'pages/hemencal.html')

def cikiszili(request):
    mixer.music.load("static/muzik/Ses/muzik3.mp3") 
    mixer.music.set_volume(sesseviyesi/100)
    mixer.music.play()
    return render(request,'pages/hemencal.html')

def istiklalmarsi(request):
    mixer.music.load("static/muzik/Resmi/istiklalmarsi.mp3") 
    mixer.music.set_volume(sesseviyesi/100)
    mixer.music.play()
    return render(request,'pages/hemencal.html')

def saygidurusu1(request):
    mixer.music.load("static/muzik/Resmi/saygi1dakika-istiklalmarsi.mp3") 
    mixer.music.set_volume(sesseviyesi/100)
    mixer.music.play()
    return render(request,'pages/hemencal.html')

def saygidurusu2(request):
    mixer.music.load("static/muzik/Resmi/saygi2dakika-istiklalmarsi.mp3") 
    mixer.music.set_volume(sesseviyesi/100)
    mixer.music.play()
    return render(request,'pages/hemencal.html')

def siren(request):
    mixer.music.load("static/muzik/Resmi/siren30saniye.mp3") 
    mixer.music.set_volume(sesseviyesi/100)
    mixer.music.play()
    return render(request,'pages/hemencal.html')